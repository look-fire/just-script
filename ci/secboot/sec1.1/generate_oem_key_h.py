#!/usr/bin/python
#Transsion Top Secret

import os
import sys
from string import Template
#s = Template('$who likes $what')

param_n = sys.argv[1]
outdir = sys.argv[2]

if len(param_n) == 514:
    param_n = param_n[2:]
elif len(param_n) == 512:
    pass
else:
    print "error: param_n length: %s" % len(param_n)
    sys.exit(1)


s = Template(r'''#ifndef __OEMKEY__
#define __OEMKEY__

/* OEM_PUBK is set as the same as MTEE public key for convenience, but they can be different */
/* OEM_PUBK will be used to verify oemkeystore, and use oemkeystore to verify images */
#define OEM_PUBK_SZ 256

#define OEM_PUBK          $line1, \
                          $line2, \
                          $line3, \
                          $line4, \
                          $line5, \
                          $line6, \
                          $line7, \
                          $line8, \
                          $line9, \
                          $line10, \
                          $line11, \
                          $line12, \
                          $line13, \
                          $line14, \
                          $line15, \
                          $line16

#endif /* __OEMKEY__ */
''')

transfered_param_n = []

for i in range(0, len(param_n)/2):
    transfered_param_n.append('0x'+param_n[i*2:i*2+2].upper())

line1 = ', '.join(transfered_param_n[0*16:0*16+16])
line2 = ', '.join(transfered_param_n[1*16:1*16+16])
line3 = ', '.join(transfered_param_n[2*16:2*16+16])
line4 = ', '.join(transfered_param_n[3*16:3*16+16])
line5 = ', '.join(transfered_param_n[4*16:4*16+16])
line6 = ', '.join(transfered_param_n[5*16:5*16+16])
line7 = ', '.join(transfered_param_n[6*16:6*16+16])
line8 = ', '.join(transfered_param_n[7*16:7*16+16])
line9 = ', '.join(transfered_param_n[8*16:8*16+16])
line10 = ', '.join(transfered_param_n[9*16:9*16+16])
line11 = ', '.join(transfered_param_n[10*16:10*16+16])
line12 = ', '.join(transfered_param_n[11*16:11*16+16])
line13 = ', '.join(transfered_param_n[12*16:12*16+16])
line14 = ', '.join(transfered_param_n[13*16:13*16+16])
line15 = ', '.join(transfered_param_n[14*16:14*16+16])
line16 = ', '.join(transfered_param_n[15*16:15*16+16])


s = s.substitute(
    line1=line1,
    line2=line2,
    line3=line3,
    line4=line4,
    line5=line5,
    line6=line6,
    line7=line7,
    line8=line8,
    line9=line9,
    line10=line10,
    line11=line11,
    line12=line12,
    line13=line13,
    line14=line14,
    line15=line15,
    line16=line16,
)

with open(os.path.join(outdir, "oemkey.h"), "w") as f:
    f.write(s)
