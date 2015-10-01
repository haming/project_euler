# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:01:40 2015

@author: ming
"""

matrix = []
with open('81 matrix.txt','r') as fh:
    for line in fh:
        matrix.append([int(num) for num in line[:-1].split(',')])
              
#matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
dim = (len(matrix),len(matrix[0]))
for l in range(1,sum(dim)-1):
    for i in range(l+1):
        if i<dim[0] and l-i<dim[1]:
            if i-1>=0:
                a = matrix[i-1][l-i]
            else:
                a = 1e6
            if l-i-1>=0:
                b = matrix[i][l-i-1]
            else:
                b = 1e6
            matrix[i][l-i] += min(a,b)
#            print(matrix[i][l-i],)
#    print()

print(matrix[dim[0]-1][dim[1]-1])