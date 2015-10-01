def isBouncy(n):
    if n < 10:
        return False
    digits = list(map(int, str(n)))
    for i in range(1, len(digits)-1):
        if (digits[0] >= digits[1]) != (digits[i]>=digits[i+1]) \
            and (digits[0] <= digits[1]) != (digits[i]<=digits[i+1]):
            return i+2
    return False
    
cnt = 0
i = 100
while True:
    t = isBouncy(i)
    if t:
#        print(i,t)
        cnt += 10**(len(str(i))-t)
        i += 10**(len(str(i))-t)
        if cnt / i >= 0.99:
            break
    else:
        i += 1
print(i, cnt)