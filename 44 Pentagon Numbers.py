from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def pentagonGen():
    plus = 4
    num = 1
    while True:
        yield num
        num += plus
        plus += 3
        
D = 0
p = pentagonGen()
pentagon = [next(p) for i in range(2000000)]

minDiff = None
for i in range(1,10000):
    for j in range(i+1,10000):
        if binary_search(pentagon[j:i+j],pentagon[i]+pentagon[j])!=-1:
            if binary_search(pentagon[j:i+j],pentagon[j]-pentagon[i])!=-1:
                if not minDiff or pentagon[j]-pentagon[i]<minDiff:
                    minDiff = pentagon[j]-pentagon[i]
                print(pentagon[i],pentagon[j],pentagon[j]-pentagon[i])