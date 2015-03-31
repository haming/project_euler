def collatz(n):
    while True:
        yield n
        if n==1:
            break
        if n%2==0:
            n /= 2
        else:
            n = 3*n+1
            
longestLen = 0
longestNum = 0
for i in xrange(1,1000000):
    c = collatz(i)
    length = 0
    for n in c:
        length += 1
    if length > longestLen:
        longestLen = length
        longestNum = i
print longestLen, longestNum