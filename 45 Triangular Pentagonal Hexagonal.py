def pentagonGen():
    plus = 4
    num = 1
    while True:
        yield num
        num += plus
        plus += 3
        
def triangleGen():
    plus = 2
    num = 1
    while True:
        yield num
        num += plus
        plus += 1
        
def hexagonalGen():
    plus = 5
    num = 1
    while True:
        yield num
        num += plus
        plus += 4
        
p = pentagonGen()
#pentagon = [p.next() for i in xrange(64000)]
t = triangleGen()
#triangle = [t.next() for i in xrange(64000)]
h = hexagonalGen()
#hexagonal = [h.next() for i in xrange(64000)]
#
#for h in hexagonal:
#    if h in pentagon:
#        if h in triangle:
#            print h

num = 3
pentagon = p.next()
triangle = t.next()
hexagonal = h.next()
while num:
    #print pentagon, triangle, hexagonal
    if pentagon == triangle == hexagonal:
        print pentagon
        num -= 1
    if pentagon<=triangle and pentagon<=hexagonal:
        pentagon = p.next()
    elif triangle<=pentagon and triangle<=hexagonal:
        triangle = t.next()
    else:
        hexagonal = h.next()

    