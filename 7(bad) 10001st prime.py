def primeHelper(primes, i):
    for p in primes:
        if i%p==0:
            return False
    return True

def prime():
    i = 3
    primes = [2]
    while True:
        if primeHelper(primes, i):
            yield(primes[-1])
            primes.append(i)
        i += 1
        
p = prime()
for i in range(10000):
    p.next()
    
print p.next()