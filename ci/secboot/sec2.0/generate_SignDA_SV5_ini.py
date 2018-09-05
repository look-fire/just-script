#!/usr/bin/python

import os
import sys
from string import Template
#s = Template('$who likes $what')

param_n = sys.argv[1][2:]
param_d = sys.argv[2][2:]
outdir = sys.argv[3]

s = Template('''[DAA private key]
; 2048
private_key_e = "0x0001, 0x0001"
private_key_d = "$key_d"
private_key_n = "$key_n"''')

transfered_param_n = []
transfered_param_d = []

for i in range(0, len(param_n)/4):
    transfered_param_n.append('0x'+param_n[i*4:i*4+4])

for i in range(0, len(param_d)/4):
    transfered_param_d.append('0x'+param_d[i*4: i*4+4])

s = s.substitute(key_d=','.join(transfered_param_d), key_n=','.join(transfered_param_n))

with open(os.path.join(outdir, "SignDA_SV5.ini"), "w") as f:
    f.write(s)
