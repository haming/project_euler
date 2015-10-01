def primeFactors(num, factors=[]):
    """Return a list of all the prime factors of num"""
    if num == 1:
        return factors
    i = 2
    while True:
        if num%i==0:
            return primeFactors(num/i,factors+[i])
        i += 1
        
        
from collections import Counter

def primeCounter(num):
    return Counter(primeFactors(num))


from operator import mul
from itertools import product
from numpy import array
                
def allFactors(num):
        """Return a list of all the factors of num
        by generating from prime factors"""
        p = primeCounter(num)
        combs = [range(i+1) for i in p.values()]
        factors = [reduce(mul,array(p.keys())**array(comb)) for comb in product(*combs)]
        factors.sort()
        return factors