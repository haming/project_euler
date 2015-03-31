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
        
totl = 0
p = prime()
while True:
    n = p.next()
    #print n
    if n > 2000000:
        break
    totl += n
    
print totl