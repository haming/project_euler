# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:21:39 2015

@author: meelo
"""
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end
    
    
def isPrime(num):
    """Return True if num is prime"""
    if num==0 or num==1:
        return False
    if num<4:
        return True
    if num%2==0:
        return False
    if num<9:
        return True
    if num%3==0:
        return False
    r = int(num**0.5)
    f = 5
    while f<=r:
        if num%f==0:
            return False
        if num%(f+2)==0:
            return False
        f += 6
    return True

primes = []
for i in range(10000):
    if isPrime(i):
        primes.append(i)
        
def isConcatPrime(a, b):
    return isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a)))

from itertools import combinations

prime2 = []
for p1, p2 in combinations(primes, 2):
    if isConcatPrime(p1, p2):
        prime2.append((p1, p2))

prime3 = []        
for p1, p2 in prime2:
    for p3 in primes:
        if p3<=p1 or p3<=p2:
            continue
#        if isConcatPrime(p1,p3) and isConcatPrime(p2,p3):
        if binary_search(prime2, (p2,p3))>=0 and binary_search(prime2, (p1,p3))>=0:
            prime3.append((p1,p2,p3))
    
prime4 = []        
for p1,p2,p3 in prime3:
    for p4 in primes:
        if p4<=p1 or p4<=p2 or p4<=p3:
            continue
#        if isConcatPrime(p4,p1) and isConcatPrime(p4,p2) and isConcatPrime(p4,p3):
        if binary_search(prime3, (p1,p2,p4))>=0 and binary_search(prime3, (p1,p3,p4))>=0 and binary_search(prime3, (p2,p3,p4))>=0:
            prime4.append((p1,p2,p3,p4))

##prime4 = []        
##for p1,p2 in prime2:
##    for p3,p4 in prime2:
##        if len(set([p1,p2,p3,p4]))<4:
##            continue
##        if isConcatPrime(p1,p3) and isConcatPrime(p1,p4) and isConcatPrime(p2,p3) and isConcatPrime(p2,p4):
##            prime4.append((p1,p2,p3,p4))
#
#    
prime5 = []        
for p1,p2,p3,p4 in prime4:
    for p5 in primes:
        if p5<=p1 or p5<=p2 or p5<=p3 or p5<=p4:
            continue
        if isConcatPrime(p5,p1) and isConcatPrime(p5,p2) and isConcatPrime(p5,p3) and isConcatPrime(p5,p4):
            prime5.append((p1,p2,p3,p4,p5))
print(min(map(sum,prime5)))