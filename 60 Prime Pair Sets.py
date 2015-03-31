# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 13:21:49 2015

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
    
primes = [num for num in range(100) if isPrime(num)]

from itertools import combinations

def isConcatPrime(a, b):
    return isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a)))
    
def uniqueNum(combs):
    unique = set()
    for comb in combs:
        for num in comb:
            unique.add(num)
    return tuple(unique)

def primeComb(num, primes=primes):
    if num == 2:
        combs = []
        for comb in combinations(primes,2):
            if isConcatPrime(*comb):
                combs.append(comb)
        return combs
    else:
        combs = primeComb(num-1)
        newCombs = []
        for newComb in combinations(combs,num-1):
#            print(newCombs)
            if len(uniqueNum(newComb))==num:
                newCombs.append(uniqueNum(newComb))
        return newCombs