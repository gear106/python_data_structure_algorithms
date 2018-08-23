# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 20:41:36 2018

@author: GEAR
"""

from Stack import *

def parChecker1(String):
    '''
    判断括号是否匹配,采用stack数据结构来实现
    '''
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
print(parChecker1('(())'))

def matches(start, stop):
    '''
    判断两个括号是否匹配,若是左边括号进栈，若是右边括号，若有对应左括号则出栈
    '''
    starts = '([{'
    stops = ')]}'
    return starts.index(start) == stops.index(stop)
def parChecker2(String):
    s = Stack()
    balanced = True
    index = 0
    while index < len(String) and balanced:
        symbol = String[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False

print(parChecker2('([])'))

    

