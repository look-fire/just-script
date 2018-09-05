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
readonly MTKSCRIPTSDIR=${SCRIPTDIR}/mtk_scripts
readonly OUTDIR=${SCRIPTDIR}/out

mkdir -p "${OUTDIR}"


# root key
if [ -e "$ROOTPRVKEY" ]
then
    echo "use custom root private key: $ROOTPRVKEY"
    cp "$ROOTPRVKEY" "${OUTDIR}"/rootprvk.pem
else
    openssl genrsa -out "${OUTDIR}"/rootprvk.pem 2048
fi

python "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/der_extractor/pem_to_der.py "${OUTDIR}"/rootprvk.pem "${OUTDIR}"/rootprvk.der

openssl rsa -in "${OUTDIR}"/rootprvk.pem -pubout > "${OUTDIR}"/rootpubk.pem
python "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/der_extractor/pem_to_der.py "${OUTDIR}"/rootpubk.pem "${OUTDIR}"/rootpubk.der


# img key
if [ -e "$IMGPRVKEY" ]
then
    echo "use custom root private key: $IMGPRVKEY"
    cp "$IMGPRVKEY" "${OUTDIR}"/imgprvk.pem
else
    openssl genrsa -out "${OUTDIR}"/imgprvk.pem 2048
fi
python "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/der_extractor/pem_to_der.py "${OUTDIR}"/imgprvk.pem "${OUTDIR}"/imgprvk.der

openssl rsa -in "${OUTDIR}"/imgprvk.pem -pubout > "${OUTDIR}"/imgpubk.pem
python "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/der_extractor/pem_to_der.py "${OUTDIR}"/imgpubk.pem "${OUTDIR}"/imgpubk.der


# generate CHIP_TEST_KEY.ini
pushd "${OUTDIR}"
    cp rootprvk.pem rootprvk.der rootpubk.pem rootpubk.der "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/cert_gen/
popd

pushd "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/cert_gen
    chmod 755 der_extractor
    ./der_extractor rootprvk.der CHIP_TEST_KEY.ini SV5_SIGN
    cp CHIP_TEST_KEY.ini "${OUTDIR}"
popd

pushd "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/cert_gen
    chmod 755 der_extractor
    ./der_extractor rootpubk.der oemkey.h ANDROID_SBC
    cp oemkey.h "${OUTDIR}"
popd

pushd "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/cert_gen
    chmod 755 der_extractor
    ./der_extractor rootpubk.der dakey.h ANDROID_SBC
    cp dakey.h "${OUTDIR}"
    sed -i 's/OEM/DA/g' "${OUTDIR}"/dakey.h
popd

pushd "${MTKSCRIPTSDIR}"/sign-image_v2/cert_chain/cert_gen
    chmod 755 der_extractor
    ./der_extractor rootprvk.der VERIFIED_BOOT_IMG_AUTH_KEY.ini ANDROID_SIGN
    cp VERIFIED_BOOT_IMG_AUTH_KEY.ini "${OUTDIR}"
popd

AUTH_PARAM_N=$(grep 'AUTH_PARAM_N =' "${OUTDIR}"/VERIFIED_BOOT_IMG_AUTH_KEY.ini | cut -d ' ' -f3)
AUTH_PARAM_D=$(grep 'AUTH_PARAM_D =' "${OUTDIR}"/VERIFIED_BOOT_IMG_AUTH_KEY.ini | cut -d ' ' -f3)

python generate_SignDA_SV5_ini.py "$AUTH_PARAM_N" "$AUTH_PARAM_D" "${OUTDIR}"
