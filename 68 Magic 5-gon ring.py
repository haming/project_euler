# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:54:21 2015

@author: ming
"""
from itertools import permutations

def conver_to_need(origin):
    result = []
    line_num = len(origin)//2
    for n in range(line_num):
        result.extend([origin[line_num+n],origin[n],origin[(n+1)%line_num]])
    return result

def X_gon_ring(num=10):
    avail_nums = range(1,num+1)
    line_num = num//2
    triplets = permutations(avail_nums, line_num+1)
    findout = []
    for triplet in triplets:
        line_sum = triplet[0] + triplet[1] + triplet[-1]
        unsed_num = set(avail_nums) - set(triplet)
        triplet = list(triplet)
        for i in range(1,line_num):
            tmp = line_sum-triplet[i]-triplet[(i+1)%line_num]
            if tmp in unsed_num and tmp>triplet[line_num]:
                unsed_num.discard(tmp)
                triplet.append(tmp)
            else:
                break
        if len(triplet)==num:
            findout.append(triplet)
    return findout

result = max((conver_to_need(c) for c in X_gon_ring(10)))