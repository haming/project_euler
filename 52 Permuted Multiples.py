def getDigits(num):
    digits = [int(d) for d in str(num)]
    digits.sort()
    return digits
    
for x in xrange(1,200000):
    digits = getDigits(x)
    for i in range(2,6):
       Xdigits = getDigits(i*x)
       if digits != Xdigits:
           break
    if digits == Xdigits:
        print x,2*x,3*x,4*x,5*x,6*x