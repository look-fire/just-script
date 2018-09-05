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


s = Template(r'''#
# MTEE Image Protection Parameter File
# Note
#    1. Value is HEX Notation and starts with 0x
#    2. Comment line starts with #
#

# Image version, <= 0xFFFF
IMG_VER      = 0x3001

# Protection Option, 0x00 or 0x01
PROT_OPTION  = 0x02

# Encrypt Parameter (IV/KEY) for AES128 Encryption, HEX Notation
#ENC_PARAM    = 0x00112233445566778899aabbccddeeffffeeddccbbaa99887766554433221100

# Decrypt Parameter (IV/KEY) for AES128 Decryption, Encrypted by MTK Platform, HEX Notation
#DEC_PARAM    = 0x03a39c05524d9d7b4f373293e550d6fd25d4235fae67a79d7447a7b5d05cd4fe

# Authentication Parameter (N, D) for RSA2048 (E=65537, 0x10001)
AUTH_PARAM_N = 0x$param_n
AUTH_PARAM_D = 0x$param_d
''')

s = s.substitute(param_n=param_n.lower(), param_d=param_d.lower())

with open(os.path.join(outdir, "VERIFIED_BOOT_IMG_AUTH_KEY.ini"), "w") as f:
    f.write(s)
