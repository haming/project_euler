from collections import Counter
from itertools import product
from operator import mul

def getPrimeFactors(num,factors=[]):
    """return the prime factors of num"""
    assert num > 0, 'input must bigger than 0'
    
    if num == 1:
        return factors[:]
    for i in xrange(2,num+1):
        if num%i==0:
            return getPrimeFactors(num/i,factors+[i])

def getAllFactors(num):
    #1 don't exist prime factor
    if num == 1:
        return [1]
    primeFactorList = getPrimeFactors(num)
    primeFactorDict = Counter(primeFactorList)
    primeList = primeFactorDict.keys()
    times = primeFactorDict.values()

    factorCombin = product(*[range(t+1) for t in times])
    #print list(factorCombin)
    factors = [reduce(mul,[primeList[i]**comb[i] for i in range(len(comb))])\
                for comb in factorCombin]
    return factors

def isAmicableNum(num):
    if num == 1:
        return False
    d = sum(getAllFactors(num)[:-1])
    return d != num and sum(getAllFactors(d)[:-1]) == num


total = 0
for i in xrange(1,10000):
    if isAmicableNum(i):
        total += i
print total
