def isPrime(num):
    if num==0 or num==1:
        return False
    for n in xrange(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
    
def circular(numStr):
    return numStr[1:]+numStr[0]
    
def isCircularPrime(num):
    numStr = str(num)
    length = len(numStr)
    while length>0:
        if isPrime(int(numStr)):
            numStr = circular(numStr)
            print numStr
            length -= 1
        else:
            return False
    return True
    
total = 0
for num in xrange(1000000):
    if isCircularPrime(num):
        print num
        total += 1
print '# Circular Prime:',total