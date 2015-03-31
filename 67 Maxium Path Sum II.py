# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 22:25:25 2015

@author: ming
"""

fh = open('67 triangle.txt')
triangleStr = fh.read()

#triangleStr = """3
#7 4
#2 4 6
#8 5 9 3"""

triangleList = [[int(num) for num in line.split(' ')] for line in triangleStr.split('\n')]

for l in range(len(triangleList)-2,-1,-1):
    for i in range(0,l+1):
        triangleList[l][i] += max(triangleList[l+1][i],triangleList[l+1][i+1])
print(triangleList[0][0])