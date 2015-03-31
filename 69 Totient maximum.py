# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 16:27:11 2015

@author: ming
"""
from fractions import Fraction

def primeFactors(num, factors=[]):
    """Return a list of all the prime factors of num"""
    if num == 1:
        return factors
    i = 2
    while True:
        if num%i==0:
            return primeFactors(num/i,factors+[i])
        i += 1

def totient(num):
    primes = set(primeFactors(num))
#    print(primes)
    result = num
    for p in primes:
        result *= (1-1/p)
    return int(result)


maxVal = 0
maxN = 0    
for num in range(2,11):
    val = Fraction(num,totient(num))
    if val>maxVal:
        maxN = num
        maxVal = val
    print(num,val)
print(maxN)