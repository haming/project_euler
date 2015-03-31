def pandigital(multiplicand, multiplier, product):
    numStr = str(multiplicand)+str(multiplier)+str(product)
    return '0' not in numStr and len(numStr) == 9 and len(set(numStr)) == 9

products = set()
for a in range(1,10):
    for b in range(1000,10000):
        if pandigital(a,b,a*b):
            products.add(a*b)
            print a,b,a*b
for a in range(10,100):
    for b in range(100,1000):
        if pandigital(a,b,a*b):
            products.add(a*b)
            print a,b,a*b
print sum(list(products))