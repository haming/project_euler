# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 17:22:33 2015

@author: ming
"""

def isPrime(num):
    """Return True if num is prime"""
    if num==0 or num==1:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
    
def genPrimes():
    n = 1
    while True:
        if isPrime(n):
            yield n
        n += 1
     
result = 1
p = genPrimes()
while True:
    prime = p.__next__()
    result *= prime    
    if result > int(1e6):
        result /= prime
        break
print(result)