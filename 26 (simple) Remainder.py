import re

REMAINDER_BIT = 2000

def remainder(num, bits=REMAINDER_BIT):
    """return the remainder of 1.0/num with bits bit"""
    numerator = 10
    remainderStr = ''
    for i in range(bits):
        remainderStr += str(numerator / num)
        numerator = (numerator % num) * 10
    return remainderStr
    
def reciprocalCycles(num):
    remainderStr = remainder(num)
    result = re.search(r'^\d*(\d+)\1+$', remainderStr)
    return result.group(1)
    
maxNum = 0
maxLen = 0
for num in range(2,1000):
    #print num
    if len(reciprocalCycles(num)) > maxLen:
        maxNum = num
        maxLen = len(reciprocalCycles(num))
        
print maxNum, maxLen