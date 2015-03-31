def isPrime(num):
    if num==0 or num==1:
        return False
    for n in xrange(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def pandigital(numStr):
    digits = [s for s in numStr]
    digits.sort()
    return digits == [str(i) for i in range(1,min(len(numStr)+1,10))]
            
for num in xrange(1,10000000):
    if isPrime(num):
        if pandigital(str(num)):
            print num