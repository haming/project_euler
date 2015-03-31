n = 600851475143

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
        
print max(findPrimeFactor(n))