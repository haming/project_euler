def isIt(num):
    return sum(int(d)**5 for d in str(num)) == num
    
i = 0
result = []
while True:
    if isIt(i):
        result.append(i)
        print i
    i += 1