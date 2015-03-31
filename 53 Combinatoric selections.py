#from scipy.misc import comb

from math import factorial

def comb(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

num = 0
for n in range(13,101):
    for r in range(1,n):
        if comb(n,r)>1000000:
            num += 1
            
print(num)