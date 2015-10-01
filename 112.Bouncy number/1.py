def isBouncy(n):
    if n < 10:
        return False
    digits = list(map(int, str(n)))
    for i in range(1, len(digits)-1):
        if (digits[0] >= digits[1]) != (digits[i]>=digits[i+1]) \
            and (digits[0] <= digits[1]) != (digits[i]<=digits[i+1]):
            return True
    return False
    
cnt = 0
i = 1
while True:
    if isBouncy(i):
        cnt += 1
    if cnt / i >= 0.9:
        print(i)
        break
    i += 1
print(cnt)