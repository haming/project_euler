def primeFactors(num, factors=[]):
    if num == 1:
        return factors
    i = 2
    while True:
        if num%i==0:
            return primeFactors(num/i,factors+[i])
        i += 1
        
        
times = 0
for num in xrange(1,160000):
    #print i
    primes = set(primeFactors(num))
    if len(primes)==4:
        times += 1
    else:
        times = 0
        
    if times==4:
        print num-3