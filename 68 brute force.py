# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:47:25 2015

@author: ming
"""

import itertools

vals=[1,2,3,4,5,6,7,8,9]

g0=lambda v: (10,v[0],v[1])
gons=[
  lambda v: (v[2],v[1],v[3]),
  lambda v: (v[4],v[3],v[5]),
  lambda v: (v[6],v[5],v[7]),
  lambda v: (v[8],v[7],v[0])
]

for p in itertools.permutations(vals):
  if all(sum(g(p))==sum(g0(p)) for g in gons):
    print()
    print(g0(p))
    for g in gons: print(g(p))