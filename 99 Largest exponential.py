# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 23:46:10 2015

@author: ming
"""
import math

nums = []
for line in open('99 base_exp.txt'):
    base, exp = line.split(',')
    nums.append(math.log(int(base),2)*int(exp))

maxNum = max(nums)
print(nums.index(maxNum)+1)

#maxIdx, maxVal = max(enumerate(nums), key=lambda t:t[1])

#import operator
#minIdx, minVal = min(enumerate(values), key=operator.itemgetter(1))
#maxIdx, maxVal = max(enumerate(values), key=operator.itemgetter(1))