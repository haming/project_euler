# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 20:24:33 2015

@author: ming
"""

result = 1
for i in range(7830457):
    result = (result*2)%10000000000
result = result*28433+1
print(str(result)[-10:])
