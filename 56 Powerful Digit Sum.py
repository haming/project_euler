def digitalSum(num):
    return sum(int(d) for d in str(num))
    
maxSum = 0
for a in xrange(1,100):
    for b in xrange(1, 100):
        if digitalSum(a**b) > maxSum:
            maxSum = digitalSum(a**b)
            print a, b, maxSum