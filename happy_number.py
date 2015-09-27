# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:04:48 2015

@author: meelo
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def digitSum(self, n):
        return sum(int(i)**2 for i in str(n))
        
    def isHappy(self, n):
        s = {n}
        while True:
            n = self.digitSum(n)
            if n == 1:
                return True
            if n in s:
                return False
            else:
                s.add(n)