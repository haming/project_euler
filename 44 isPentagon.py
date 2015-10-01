"""
Using root formula to get n in terms of p
if p is a pentagon then the n must be a integer
using the fact to determine wether a number is a pentago in constant time
"""
def isPentagon(p):
    return (1+(1+24*p)**0.5)%6 == 0

def pentagon(n):
    return n*(3*n-1)//2

n = 2
while True:
    pi = pentagon(n)
    for i in range(1,n-1):
        pj = pentagon(i)
        if isPentagon(pi-pj) and isPentagon(pi+pj):
            print(pi,pj,pi-pj,pi+pj)
            break
    else:
        n += 1
        continue
    break