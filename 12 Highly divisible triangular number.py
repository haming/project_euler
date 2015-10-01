from collections import Counter

#def factor(num):
#    factors = [True]*num
#    for i in xrange(1,num+1):
#        if not(factors[i-1]):
#            continue
#        if num%i != 0:
#            for n in xrange(i,num,i):
#                factors[n-1] = False
#    return sum(factors)

def primeFact(num,factors=[]):
    """return the prime factors of num"""
    if num == 1:
        return factors[:]
    for i in xrange(2,num+1):
        if num%i==0:
            return primeFact(num/i,factors+[i])

def getNumFactor(factorDict):
    """Assume factorDict a dict with key the prime factor
    values number of time the factor occur

    return the number of factors the num has
    eg: factorDict={2:3,7:2,13:1}
    will return (3+1)*(2+1)*(1+1)=24"""
    return reduce((lambda x,y:x*y),[i+1 for i in factorDict.values()])

def triangular():
    num = 1
    i = 2
    while True:
        yield num
        num += i
        i += 1


tri = triangular()
tri.next()
while True:
    num = tri.next()
    factors = primeFact(num)
    factorDict = Counter(factors)
    numFactor = getNumFactor(factorDict)
    if numFactor>500:
        print num
        break
