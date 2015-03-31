# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 19:17:17 2015

@author: ming
"""

passcode = []

def attempt(key):
    if key[0] not in passcode:
        passcode.append(key[0])
    if key[1] not in passcode:
        passcode.append(key[1])
    elif passcode.index(key[1]) < passcode.index(key[0]):
        passcode.remove(key[1])
        passcode.insert(passcode.index(key[0]),key[1])
    if key[2] not in passcode:
        passcode.append(key[2])
    elif passcode.index(key[2]) < passcode.index(key[1]):
        passcode.remove(key[2])
        passcode.insert(passcode.index(key[1]),key[2])

for i in range(10):
    key = input('Input a key:')
    attempt(key)
    print(passcode)