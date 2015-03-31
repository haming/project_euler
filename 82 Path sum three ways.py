# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:44:47 2015

@author: ming
"""

matrix = []
with open('81 matrix.txt','r') as fh:
    for line in fh:
        matrix.append([int(num) for num in line[:-1].split(',')])
              
matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
dim = (len(matrix),len(matrix[0]))

paths 