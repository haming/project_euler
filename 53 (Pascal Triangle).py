# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:02:45 2015

@author: ming
"""
count = 0
c = [[1]]

for n in range(1,101):
    cn = [1]+[0]*(n-1)+[1]
    for r in range(1,n):
        cn[r] = c[n-1][r-1]+c[n-1][r]
        if cn[r]>1000000:
            count += 1
            cn[r] = 1000000
    c.append(cn)
    
print(count)