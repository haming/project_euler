"""
Using hash table to determine wether a number is a pentagon in constant time
Also using the fact p_n<p_2n/2
"""
d = {}
l = []
n = 1
def pentagon(n):
    return n*(3*n-1)//2
    
while True:
    p = pentagon(n)
    d[p] = 1
    l.append(p)
    n += 1
    if n%2==0:
        continue
    cur = l[n//2]
    for prev in l[:n//2]:
        if cur!=2*prev and (cur-prev) in d and (cur+prev) in d:
            print(cur,prev,cur-prev,cur+prev)
            break
    else:
        continue
    break