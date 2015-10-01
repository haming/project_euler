# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 00:33:36 2015

@author: ming
"""
"""
1.with minumun information
2.can handle repeat digits
"""

fh = open('79 keylog.txt')
passlogs = fh.read()*2
#class blob(object):
#    def __init__(self,value):
#        self.value = value
#        
#    def connect(self,other):
#        pass
#    
#    def __str__(self):
#        return self.value

conns = []

def isConnect(a,b):
    afters = []
    for conn in conns:
        if conn[0]==a:
            if conn[1]==b:
                return True
            afters.append(conn[1])
    for after in afters:
        return isConnect(after,b)
    return False



for line in passlogs.split('\n'):
    a,b,c = line[0:3]
    if not isConnect(a,b):
        conns.append((a,b))
    if not isConnect(b,c):
        conns.append((b,c))
    if (a,c) in conns:
        conns.remove((a,c))
#    print(line,conns)
print(conns)

#passcode = []
#passcode.extend(conns[0])
#conns.remove(conns[0])
#while conns:
#    for conn in conns:
#        if passcode[-1]==conn[0]:
#            passcode.append(conn[1])
#            conns.remove(conn)
#        if passcode[0]==conn[1]:
#            passcode.insert(0,conn[0])
#            conns.remove(conn)
#        print(conns)
#print(passcode)