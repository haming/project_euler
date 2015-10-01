import time

def numberLetter(num):
    numBit = [int(i) for i in str(num)]
    numBit.reverse()

    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    dozens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    hundreds = [''] + [i+' hundred' for i in ones[1:]]
    thousands = [''] + [i+' thousand' for i in ones[1:]]
    bits = [ones,tens,hundreds, thousands]

    numStr = ''

    if 10<num%100<20:
        numStr = dozens[num%100-10] + numStr
    else:
        numStr = ones[num%10] + numStr
        if (num/10)%10:
            numStr = tens[(num/10)%10] + ' ' + numStr

    if num%100 and num/100:
        numStr = 'and ' + numStr

    if (num/100)%10:
        numStr = ones[(num/100)%10] + ' hundred ' + numStr

    if (num/1000)%10:
        numStr = ones[(num/1000)%10] + ' thousand ' + numStr
    return numStr.strip(' ')

numLen = 0
for i in xrange(1,1001):
    numLen += len(numberLetter(i).replace(' ',''))
print numLen
