#!/bin/bash
#Transsion Top Secret
#  commonlibs.sh: common bash function libs
#  DO NOT PUT CODE OTHER THAN FUNCTIONS
#  NO GLOBAL ENVIRONMENT VARIABLES ALLOWED

function myrealpath(){
    local -r path="$1"
    if [ ! -z "${path}" ]
    then
        python -c "import os; print os.path.abspath('${path}')"
    else
        echo ""
    fi
}

function is_safe_path(){
    local -r path="$1"
    python - "${path}" <<EOF
import sys
if len(sys.argv[1]) == 0:
    sys.exit(1)
validchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+,-./@_'
result = all(c in validchars for c in sys.argv[1])
if result:
    sys.exit(0)
else:
    sys.exit(1)
EOF
    return $?
}


function is_safe_utf8_path(){
    local -r path="$1"
    python - "${path}" <<EOF
import sys
path = sys.argv[1]
if len(path) == 0:
    sys.exit(1)
valid_utf8 = True
try:
    path.decode('utf-8')
except UnicodeDecodeError:
    valid_utf8 = False
if not valid_utf8:
    sys.exit(1)

invalidchars = '<>:|=' + "\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x5C\x60"
result = any(c in invalidchars for c in path)
if result:
    sys.exit(1)
else:
    sys.exit(0)
EOF
    return $?
}


function is_safe_name_component(){
    local -r component="$1"
    python - "${component}" <<EOF
import sys
if len(sys.argv[1]) == 0:
    sys.exit(1)
validchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+,-.@_'
result = all(c in validchars for c in sys.argv[1])
if result:
    sys.exit(0)
else:
    sys.exit(1)
EOF
    return $?
}

function is_safe_verison_name(){
    local -r component="$1"
    python - "${component}" <<EOF

import sys
import re

if len(sys.argv[1]) == 0:
    sys.exit(1)
result=re.search('^[A-Z,a-z].*-.*V.*\d$',sys.argv[1])
if result:
    sys.exit(0)
else:
    sys.exit(1)
EOF
    return $?
}


function is_safe_url(){
    local -r component="$1"
    python - "${component}" <<EOF
import sys
if len(sys.argv[1]) == 0:
    sys.exit(1)
validchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+,-._:/'
result = all(c in validchars for c in sys.argv[1])
if result:
    sys.exit(0)
else:
    sys.exit(1)
EOF
    return $?
}


function is_safe_windows_user(){
    local -r user="$1"
    python - "${user}" <<EOF
import sys
if len(sys.argv[1]) == 0:
    sys.exit(1)
validchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._/'
result = all(c in validchars for c in sys.argv[1])
if result:
    sys.exit(0)
else:
    sys.exit(1)
EOF
    return $?
}


function is_safe_utf8_windows_path(){
    local -r path="$1"
    python - "${path}" <<EOF
import sys
path = sys.argv[1]
if len(path) == 0:
    sys.exit(1)
valid_utf8 = True
try:
    path.decode('utf-8')
except UnicodeDecodeError:
    valid_utf8 = False
if not valid_utf8:
    sys.exit(1)

invalidchars = '<>:|=/' + "\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x60"
result = any(c in invalidchars for c in path)
if result:
    sys.exit(1)
else:
    sys.exit(0)
EOF
    return $?
}


function log(){
    local -r MODE=$1
    shift
    echo "$(date '+%Y-%m-%d %H:%M:%S') ${MODE}: $*"
}


function log_info(){
    log "INFO" "$@"
}


function log_warning(){
    log "WARNING" "$@"
}


function log_error(){
    # NOTICE: when calling log_error, the build process should be regarded as failure
    log "ERROR" "$@"
}


function all_switch(){
    for arg in "$@"
    do
        if [[ "$arg" != "true" && "$arg" != "false" ]]
        then
            return 1
        fi
    done
    return 0
}


function is_file_confidential(){
    local -r file="$1"
    if [[ "${file}" == *'.java' || "${file}" == *'.c' || "${file}" == *'.cpp' || "${file}" == *'.cc' \
          || "${file}" == *'.h' ||  "${file}" == *'.cxx' || "${file}" == *'.CPP' || "${file}" == *'.c++' \
          || "${file}" == *'.hh' || "${file}" == *'.py' || "${file}" == *'.sh' ]]
    then
        return 0
    else
        return 1
    fi
}


