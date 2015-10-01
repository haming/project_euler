import operator

s = ''.join([str(num) for num in range(1,500000)])
print reduce(operator.mul, [int(s[10**i-1])for i in range(0,7)])