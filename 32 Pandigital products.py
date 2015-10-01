def pandigital(multiplicand, multiplier, product):
    numStr = str(multiplicand)+str(multiplier)+str(product)
    return '0' not in numStr and len(numStr) == 9 and len(set(numStr)) == 9
    
products = set()
for a in range(1,1000):
    #print 'a=', a
    for b in range(a,10000):
        if a*b > 987654321:
            break
        if pandigital(a,b,a*b):
            products.add(a*b)
            print a,b,a*b
            
print sum(list(products))