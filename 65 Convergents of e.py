# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 19:50:20 2015

@author: ming
"""

from fractions import Fraction

def approx(seq):
    frac = Fraction(1,seq[-1])
    seq.reverse()
    for n in seq[1:]:
        frac = 1/(n+frac)
#        print(frac)
    return 1/frac
    
def gen_e_seq():
    """e=[2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]"""
    seq = [2]
    for i in range(1,34):
        seq.append(1)
        seq.append(2*i)
        seq.append(1)
    return seq

result = approx(seq)
print(result)
print(sum(int(d) for d in str(result.numerator)))