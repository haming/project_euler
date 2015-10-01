def powerfulDigit(n): 
    i = 1
    count = 0
    while True:
        length = len(str(i**n))
        if length==n:
            print '%s^%s' % (i,n)
            count += 1
        elif length>n:
            return count
        i += 1
    
count = 0
for i in xrange(100):
    count += powerfulDigit(i)
print count