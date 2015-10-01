# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 17:31:01 2015

@author: ming
"""
def gcd(a, b):
    """Return the greatest common divide of a and b"""
    if a == 0:
        return b
    else:
        return gcd(b%a,a)

minErr = float('inf')
minFrac = None
for fm in range(8, 1000000):
    fz = 3.0/7*fm
    fzInt = int(fz)
    if gcd(fm, fzInt) == 1:
        err = 3.0/7 - fzInt/float(fm)
        if err < minErr:
            minErr = err
            minFrac = (fzInt, fm)