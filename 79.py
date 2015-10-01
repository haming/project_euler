# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 13:37:01 2015

@author: ming
"""

mapr=[[0 for i in range(10)] for j in range(10)]
def map():
  data="319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716"
  data1=data.split(",")
  for d in data1:
    mapr[int(d[0])][int(d[1])]=1
    mapr[int(d[0])][int(d[2])]=1
    mapr[int(d[1])][int(d[2])]=1

def show():
  for i in range(10):
  	print("\n",i,"-->",)
  	for j in range(10):
  	  if mapr[i][j]:
  	  	print(j,)

map()
show()