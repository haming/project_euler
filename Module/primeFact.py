from collections import Counter

def primeFact(num,factors=[]):
    if num == 1:
        return factors[:]
    for i in xrange(2,num+1):
        if num%i==0:
            return primeFact(num/i,factors+[i])

factors = primeFact(1000)
factDict = Counter(factors)
