# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 22:12:54 2015

@author: ming
"""

from Module.primeFactors import allFactors

def abundantNum(num):
    return sum(allFactors(num)[:-1]) > num
    
    
abundantNums = [n for n in xrange(2,28124) if abundantNum(n)]

abundantNumSums = set()
for i in xrange(len(abundantNums)):
    for j in xrange(i,len(abundantNums)):
        abundantNumSums.add(abundantNums[i]+abundantNums[j])
            
#print abundantNumSums

total = 0
for n in xrange(28124):
    if n not in abundantNumSums:
        print n
        total += n
print 'total=', total