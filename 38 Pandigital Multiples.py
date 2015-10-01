def pandigital(numStr):
    return '0' not in numStr and len(numStr) == 9 and len(set(numStr)) == 9
    
def concatenatProduct(num):
    numStr = ''
    n = 1
    while len(numStr) < 9:
        numStr += str(num*n)
        n += 1
    return numStr
    
for num in range(10000):
    if pandigital(concatenatProduct(num)):
        print num,concatenatProduct(num)