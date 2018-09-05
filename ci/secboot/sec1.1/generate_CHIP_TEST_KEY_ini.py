#!/usr/bin/python
#Transsion Top Secret

import os
import sys
from string import Template

param_n = sys.argv[1]
param_d = sys.argv[2]
outdir = sys.argv[3]

if len(param_n) == 514:
    param_n = param_n[2:]
elif len(param_n) == 512:
    pass
else:
    print "error: param_n length: %s" % len(param_n)
    sys.exit(1)

if len(param_d) == 514:
    param_d = param_d[2:]
elif len(param_d) == 512:
    pass
else:
    print "error: param_d length: %s" % len(param_d)
    sys.exit(1)

s = Template(r'''; #################################
; Code Signature Key
; #################################

[Code Sig Key]
; Hex format
private_key_d = "$param_d"
private_key_n = "$param_n"
public_key_e  = "00010001"
public_key_n  = "$param_n"

[Install Sig Key]
public_key_e  = "00010001"
public_key_n  = "$param_n"

; #################################
; Anticlone key
; #################################

[Anticlone key]
; Customer's anticlone key in BB chip
; Hex format
anticlone_key = "0x11111111, 0x22222222, 0x33333333, 0x44444444"
''')

s = s.substitute(param_n=param_n.upper(), param_d=param_d.upper())

with open(os.path.join(outdir, "CHIP_TEST_KEY.ini"), "w") as f:
    f.write(s)
