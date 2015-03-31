def isPrime(num):
    if num==0 or num==1:
        return False
    for n in xrange(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

primes = [num for num in range(1000,10000) if isPrime(num)]

from itertools import combinations, permutations

def permutNumGen(num):
    for p in permutations(str(num)):
        yield int(''.join(p))
        
def isArithmeticSeq(l):
    newL = sorted(l)
    difference = newL[1]-newL[0]
    for i in range(1,len(l)-1):
        if (newL[i+1]-newL[i])!=difference:
            return False
    return True


for prime in primes:
    permutNum = list(set(permutNumGen(prime)))
    primePermutNum = [num for num in permutNum if isPrime(num) and len(str(num))==4]
    if len(primePermutNum)>=3:
        for comb in combinations(primePermutNum,3):
            if isArithmeticSeq(comb):
                print comb