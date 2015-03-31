# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 19:50:20 2015

@author: ming
"""

from fractions import Fraction
    
def gen_e_seq():
    """seq=[2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]"""
    seq = [2]
    for i in range(1,34):
        seq.extend([1,2*i,1])
    return seq

def approx(seq):
    """Approximate a number by computing infinite continued fraction"""
    frac = Fraction(1,seq[-1]) #Computing inter fraction first
    for n in reversed(seq[:-1]): #in reverse order
        frac = 1/(n+frac)
    return 1/frac
    
result = approx(gen_e_seq())
print(sum(int(d) for d in str(result.numerator)))