def isPrime(num):
    if num==0 or num==1:
        return False
    for n in xrange(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
    
def truncate(num, direction='right'):
    if len(str(num)) == 1:
        return float('NaN')
    if direction == 'right':
        return int(str(num)[:-1])
    if direction == 'left':
        return int(str(num)[1:])
        
def truncatePrime(num, direction='right'):
    length = len(str(num))
    while length>0:
        #print num
        if isPrime(num):
            num = truncate(num, direction)
            length -= 1
        else:
            return False
    return True
    
total = 0
for num in range(1000000):
    if truncatePrime(num,'right') and truncatePrime(num,'left'):
        if num>10:
            total += num
            print num
print 'total =', total