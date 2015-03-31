# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:42:43 2015

@author: ming
"""

direction = [(1,0),(0,1),(-1,0),(0,-1)]
times = 1

def nextDirect():
    direction = 0
    n = 0
    while True:
        repeat = n//2+1
        for i in range(repeat):
            yield direction
        direction = (direction+1)%4
        n += 1

def position():
    position = (0,0)
    n = nextDirect()
    while True:
        yield position
        direct = direction[n.__next__()]
        position = (position[0]+direct[0], position[1]+direct[1])
        
def isPrime(num):
    """Return True if num is prime"""
    if num==0 or num==1:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
    

p = position()
total = 0
n = 100000
for num in range(1, n*n+1):
    pos = p.__next__()
    if abs(pos[0]) == abs(pos[1]):
        if isPrime(num):
            total += 1
    if pos[0]==(-pos[1]):
        sideLen = int(num**0.5)
        ratio = total/(2*sideLen-1)
        print(sideLen,ratio)
        if ratio!=0 and ratio < 0.1:
            break

