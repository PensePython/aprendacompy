#!/usr/bin/env python

from keyword import kwlist

comp = 0
for k in kwlist:
    if len(k)>comp: comp = len(k)
fmt = ' %-'+str(comp)+'s'
for i in range(5):
    for j in range(6):
        if (i+j*5) >= len(kwlist): break
        print fmt % kwlist[i+j*5],
    print
    if (i+j*5) >= len(kwlist): break
