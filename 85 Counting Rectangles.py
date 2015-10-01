# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 21:54:27 2015

@author: ming
"""

def countRect(m,n):
    total = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
#            print(i,j,(m+1-i)*(n+1-j))
            total += (m+1-i)*(n+1-j)
    return total

h,w = 1,1
diff = 2000000
    
for i in range(1,1450):
    for j in range(i,1450):
        if abs(2000000-countRect(i,j))<diff:
            h,w=i,j
            diff = abs(2000000-countRect(i,j))