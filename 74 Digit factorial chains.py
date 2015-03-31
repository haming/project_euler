# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:17:55 2015

@author: ming
"""
from math import factorial

def nextNum(num):
    return sum(factorial(int(d)) for d in str(num))
    
lenDict = {}
def digit_factorial_chain(num):
    chain = [num]
    length = 1
    while True:
        num = nextNum(num)
        if num in lenDict:
            length += lenDict[num]
            break
        if num not in chain:
            chain.append(num)
            length += 1
        else:
            break
    return length

count = 0
for i in range(1000000):
    length = digit_factorial_chain(i)
    if i<100:
        lenDict[i] = length
    if length == 60:
        count += 1
        print(i)
print('count:',count)