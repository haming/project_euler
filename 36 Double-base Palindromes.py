def isPal(s):
    if len(s)<=1:
        return True
    return s[0]==s[-1] and isPal(s[1:-1])
    
def doubleBasePal(num):
    return isPal(str(num)) and isPal(bin(num)[2:])
    
total = 0
for num in xrange(1000000):
    if doubleBasePal(num):
        total += num

print 'total =',total