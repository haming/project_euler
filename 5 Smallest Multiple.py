def findPrimeFactor(n, primes=[]):
    if n == 1:
        return primes
    i = 2
    while True: 
        if n%i == 0:
            #print n,i,primes
            newPrimes = primes + [i]
            return findPrimeFactor(n/i,newPrimes)
        i += 1
        
def toDict(numList):
    d = {}
    for l in numList:
        d[l] = d.get(l,0) + 1
    return d
    
wholePrimeDict = {}
for i in range(1,21):
    primeList = findPrimeFactor(i)
    occurDict = toDict(primeList)
    for l in occurDict:
        if occurDict[l] > wholePrimeDict.get(l,0):
            wholePrimeDict[l] = occurDict[l]
            
product = 1
for l in wholePrimeDict:
    product *= l**wholePrimeDict[l]
print product