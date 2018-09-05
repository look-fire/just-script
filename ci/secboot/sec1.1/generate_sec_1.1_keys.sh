#!/bin/bash
#Transsion Top Secret

function parse_options(){
    unset ROOTPRVKEY
    unset IMGPRVKEY
    # NOTICE: try out best to transform directory paths to absolute paths(e.g. './' -> '/home/user/mycode')
    while [[ $# -gt 1 ]]
    do
        key="$1"

        case "$key" in
            --rootprvkey)
                readonly ROOTPRVKEY="$2"
                if [ ! -f "$ROOTPRVKEY" ]
                then
                    echo "root private key does not exist: $ROOTPRVKEY, exit abnormally"
                    exit 1
                fi
                ;;
            --imgprvkey)
                readonly IMGPRVKEY="$2"
                if [ ! -f "$IMGPRVKEY" ]
                then
                    echo "img private key does not exist: $IMGPRVKEY, exit abnormally"
                    exit 1
                fi
                ;;
        esac
        shift; shift # past option, do not support regular argument
    done
}

parse_options "$@"

readonly SCRIPTDIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
readonly OUTDIR=${SCRIPTDIR}/out

rm -rf "$OUTDIR"
mkdir -p "$OUTDIR"

# root key
if [ -e "$ROOTPRVKEY" ]
then
    echo "use custom root private key: $ROOTPRVKEY"
    cp "$ROOTPRVKEY" "${OUTDIR}"/rootprvk2048.pem
else
    openssl genrsa -out "${OUTDIR}"/rootprvk2048.pem 2048
fi
openssl rsa -text -in "${OUTDIR}"/rootprvk2048.pem -pubout > "${OUTDIR}"/rootkey2048.txt
openssl rsa -in "${OUTDIR}"/rootprvk2048.pem -pubout > "${OUTDIR}"/rootpub2048.pem

# img key
if [ -e "$IMGPRVKEY" ]
then
    echo "use custom root private key: $IMGPRVKEY"
    cp "$IMGPRVKEY" "${OUTDIR}"/imgprvk1024.pem
else
    openssl genrsa -out "${OUTDIR}"/imgprvk1024.pem 1024
fi
openssl rsa -text -in "${OUTDIR}"/imgprvk1024.pem -pubout > "${OUTDIR}"/imgkey1024.txt


# parse key
AUTH_PARAM_N_ROOT_2048=$(head -20 "${OUTDIR}"/rootkey2048.txt |tail -18|sed 's/ //g'|sed 's/://g'|sed ':a;N;$!ba;s/\n//g')
AUTH_PARAM_D_ROOT_2048=$(head -40 "${OUTDIR}"/rootkey2048.txt |tail -18|sed 's/ //g'|sed 's/://g'|sed ':a;N;$!ba;s/\n//g')
AUTH_PARAM_N_IMG_1024=$(head -11 "${OUTDIR}"/imgkey1024.txt |tail -9|sed 's/ //g'|sed 's/://g'|sed ':a;N;$!ba;s/\n//g')
AUTH_PARAM_D_IMG_1024=$(head -22 "${OUTDIR}"/imgkey1024.txt |tail -9|sed 's/ //g'|sed 's/://g'|sed ':a;N;$!ba;s/\n//g')

# preloader/oem
python generate_cust_sec_ctrl_h.py "$AUTH_PARAM_N_ROOT_2048" "${OUTDIR}"

# lk/oem key
python generate_oem_key_h.py "$AUTH_PARAM_N_ROOT_2048" "${OUTDIR}"

# VERIFIED_BOOT_IMG_AUTH_KEY.ini
python generate_VERIFIED_BOOT_IMG_AUTH_KEY_ini.py "$AUTH_PARAM_N_ROOT_2048" "$AUTH_PARAM_D_ROOT_2048" "${OUTDIR}"

# CHIP_TEST_KEY.ini
python generate_CHIP_TEST_KEY_ini.py "$AUTH_PARAM_N_ROOT_2048" "$AUTH_PARAM_D_ROOT_2048" "${OUTDIR}"

# IMG_AUTH_KEY.ini
python generate_IMG_AUTH_KEY_ini.py "$AUTH_PARAM_N_IMG_1024" "$AUTH_PARAM_D_IMG_1024" "${OUTDIR}"

# SignDA_SV5.ini
python generate_SignDA_SV5_ini.py "$AUTH_PARAM_N_ROOT_2048" "$AUTH_PARAM_D_ROOT_2048" "${OUTDIR}"

