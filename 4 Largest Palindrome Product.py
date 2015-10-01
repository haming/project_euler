def isPal(s):
    if len(s)<=1:
        return True
    return s[0]==s[-1] and isPal(s[1:-1])
    
res = None
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i*j
        if isPal(str(num)):
            if res == None or num > res:
                res = num
print res