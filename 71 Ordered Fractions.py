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

class fraction(object):
    def __init__(self,n,d):
        self.n = n
        self.d = d
        
    def __lt__(self, other):
        return self.n/self.d < other.n/other.d
        
    def __eq__(self, other):
        return self.n==other.n and self.d==other.d
        
    def isReduced(self):
        return gcd(self.n, self.d)==1
        
    def __str__(self):
        return '%s/%s' % (self.n,self.d)
        
fractions = []
precision = 8
lower = int(3/7*(10**precision))
higher = lower+1
bits = 10**precision
for d in range(2,1000001):
    for n in range(1,d):
        f = fraction(n,d)
        if fraction(lower,bits)<f<fraction(higher,bits):
            if f.isReduced():
                print(f)
                fractions.append(f)
            
fractions.sort()
fractions.index(fraction(3,7))