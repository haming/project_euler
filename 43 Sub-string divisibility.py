import time
import itertools
from string import digits

starttime = time.time()

    
def subStrDiv(numStr):
    divisors = [2,3,5,7,11,13,17]
    for i in range(7,0,-1):
        if int(numStr[i:i+3])%divisors[i-1] != 0:
            return False
    return True
    
total = 0
for d in itertools.permutations(digits):
    if d[0] == '0' or d[5] != '5':
        continue
    numStr = ''.join(d)
    if subStrDiv(numStr):
        total += int(numStr)
print total

print (time.time() - starttime), "seconds"