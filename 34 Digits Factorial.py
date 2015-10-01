# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 22:35:58 2015

@author: ming
"""
from math import factorial

def digitFactorial(num):
    return sum(factorial(int(d)) for d in str(num))
    
total = 0
for num in xrange(10,100000):
    t = digitFactorial(num)
    if t == num:
        total += t
        print t
print 'total=', total