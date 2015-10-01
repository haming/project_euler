def isPal(s):
    if len(s)<=1:
        return True
    return s[0]==s[-1] and isPal(s[1:-1])
    
def isLychrel(num):
    for i in xrange(50):
        num = num + int(str(num)[::-1])
        if isPal(str(num)):
            return False
    return True
    
num = 0
for i in xrange(10000):
    if isLychrel(i):
        #print i
        num += 1
print num