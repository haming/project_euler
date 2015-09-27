# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:24:56 2015

@author: meelo
"""    
count = 0
for n in range(10**9):
    if n%10==0:
        continue
    
    s = str(n)
    if s[0]&1==s[-1]:
        continue
    if 

    n_rn = n + int(''.join(reversed(str(n))))
        
    if all(int(d)%2==1 for d in str(n_rn)):
        count += 1