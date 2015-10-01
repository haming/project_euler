# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 15:54:56 2015

@author: ming
"""
import re

def isPrime(num):
    """Return True if num is prime"""
    if num==0 or num==1:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
    
primes = [str(n) for n in range(10000,100000) if isPrime(n)]

for p in primes:
    
    pattern = re.compile(r'')
    results = pattern.findall(','.join(primes))
    if len(results)==7:
        print(results)
