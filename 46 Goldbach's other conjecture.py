def isPrime(num):
    if num==0 or num==1:
        return False
    for n in xrange(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
    

def genPrimes():
    num = 1
    while True:
        if isPrime(num):
            yield num
        num += 1

        
def goldbach(num):
    p = genPrimes()
    prime = p.next()
    while prime<=num:
        t = ((num-prime)/2.0)**0.5
        if int(t)==t:
            #return prime,t
            return True
        prime = p.next()
    return False
    
def canBeWritten(num):
    i = 0
    while 2*i*i<num:
        if isPrime(num-2*i*i):
            return True
        i += 1
    return False

for num in range(3,6400,2):
    if not canBeWritten(num):
        print num