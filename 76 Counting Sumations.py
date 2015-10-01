# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:26:37 2015

@author: ming
"""

def nextComb(comb):
    for i in range(1,len(comb)):
        comb1 = comb[:]
        if comb1[0]-comb1[1]>=2 and comb1[i-1]-comb1[i]>=2:
            comb1[0]-=1
            comb1[i]+=1
            yield comb1


num = 12
ways = 0
for l in range(num-1,0,-1):
    comb = [l]+[1]*(num-l)
    i = 1
    fifo = [comb]
    while fifo:
        comb1 = fifo.pop(0)
        print(comb1)
        if comb1[0]-comb1[1]>=2 and comb1[i-1]-comb1[i]>=2:
            comb1[0]-=1
            comb1[i]+=1
            fifo.append(comb1[:])
        else:
            i += 1
            if i==len(comb):
                break