# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:12:48 2015

@author: ming
"""

count = 0
c = [1]

for n in range(1,1001):
    t = c[:]
    for r in range(1,n):
        t[r] = c[r-1]+c[r]
        if t[r]>1000000:
            count += 1
            t[r] = 1000000
    t.append(1)
    c = t[:]
    
print(count)