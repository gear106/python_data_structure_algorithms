# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 18:30:24 2018

@author: GEAR
"""

from Deque import *

def palchecker(aString):
    
    charDeque = Deque()
    for s in aString:
        charDeque.addFront(s)
    stillEqual = True
    
    while charDeque.size() > 1 and stillEqual:
        if charDeque.removeFront() != charDeque.removeRear():
            stillEqual = False
    return stillEqual

if __name__ == "__main__":
    s = 'boobs'
    print(palchecker(s))