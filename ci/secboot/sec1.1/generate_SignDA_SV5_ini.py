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

s = Template(r'''[DAA private key]
; 2048
private_key_e = "0x0001, 0x0001"
private_key_d = "$key_d"
private_key_n = "$key_n"
''')

key_n = []
key_d = []

for i in range(0, len(param_n)/4):
    key_n.append('0x'+param_n[i*4:i*4+4])

for i in range(0, len(param_d)/4):
    key_d.append('0x'+param_d[i*4: i*4+4])

s = s.substitute(key_d=', '.join(key_d), key_n=', '.join(key_n))

with open(os.path.join(outdir, "SignDA_SV5.ini"), "w") as f:
    f.write(s)
