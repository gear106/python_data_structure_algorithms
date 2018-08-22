# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 20:41:36 2018

@author: GEAR
"""
'''
判断括号是否匹配
'''
from Stack import *

def parChecker(String):
    s = Stack()
    balanced = True
    index = 0
    while index < len(String) and balanced:
        symbol = String[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False
print(parChecker('(())'))
