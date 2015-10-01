# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 20:58:42 2015

@author: ming
"""

def squareDigits(num):
    return sum([int(d)**2 for d in str(num)])
    
mem89 = [2, 4, 16, 37, 3, 9, 5, 25, 29, 6, 36, 45, 41, 17, 8, 11, 12, 14, 15, 26, 40, 18, 20, 21, 22, 24, 27, 34, 30, 33, 35, 38, 39, 42, 43, 46, 47, 48]

def endWith89(num, mem89):
    path = []
    while True:
        path.append(num)
        num = squareDigits(num)        
        if num==89 or num in mem89:
#            for n in path:
#                if n not in mem89 and n<50:
#                    mem89.append(n)
            return 89
        if num==1:
            return 1
            
total = 0
for num in range(1,10000000):
    if endWith89(num, mem89)==89:
        total += 1
print(total)