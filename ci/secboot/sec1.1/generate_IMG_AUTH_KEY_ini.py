#!/usr/bin/python
#Transsion Top Secret

import os
import sys
from string import Template

param_n = sys.argv[1]
param_d = sys.argv[2]
outdir = sys.argv[3]

if len(param_n) == 258:
    param_n = param_n[2:]
elif len(param_n) == 256:
    pass
else:
    print "error: param_n length: %s" % len(param_n)
    sys.exit(1)

if len(param_d) == 258:
    param_d = param_d[2:]
elif len(param_d) == 256:
    pass
else:
    print "error: param_d length: %s" % len(param_d)
    sys.exit(1)

s = Template(r'''CUSTOM_RSA_N = 0x$param_n
CUSTOM_RSA_D = 0x$param_d
CUSTOM_RSA_E = 0x10001
''')

s = s.substitute(param_n=param_n.lower(), param_d=param_d.lower())

with open(os.path.join(outdir, "IMG_AUTH_KEY.ini"), "w") as f:
    f.write(s)
