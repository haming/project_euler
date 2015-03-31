import re
from decimal import *

getcontext().prec = 10000
getcontext().rounding = 'ROUND_DOWN'

def reciprocalCycles(num):
    decimalNum = (Decimal(1)/Decimal(num)).quantize(Decimal('1.'+'0'*10000))
    result = re.search(r'^\d*(\d+)\1+$', str(decimalNum)[2:])
    return result.group(1)

maxNum = 0
maxLen = 0
for num in range(2,1000):
    #print num
    if len(reciprocalCycles(num)) > maxLen:
        maxNum = num
        maxLen = len(reciprocalCycles(num))
        
print maxNum, maxLen