availCoin = [200, 100, 50, 20, 10, 5, 2, 1]
want = 200

nums = [0] * 8

def dot(a, b):
    return sum(a[i]*b[i] for i in xrange(len(a)))
        
def findCoin(left, coin, makeup=[]):
    #print left,makeup,coin
    if left == 0:
        #print makeup
        return [makeup]
    if coin == []:
        #print makeup
        return [[]]
    allSols = []
    for i in range(left/coin[0]+1):
        #print left/coin[0]+1,i,left-coin[0]*i,makeup+[coin[0]]*i
        #print coin[0]
        solutions = findCoin(left-coin[0]*i,coin[1:],makeup+[coin[0]]*i)
        #print solutions
        for solution in solutions:
            if solution:
                allSols += [solution]
    return allSols[:]
solutions = findCoin(200,availCoin)
print 'solutions', len(solutions)