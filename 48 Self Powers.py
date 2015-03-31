s = 0
tenToTen = 10**10
for i in xrange(1,1001):
    s += i**i % tenToTen
print str(s)[-10:]


str(sum([i**i for i in range(1,1001)]))[-10:]