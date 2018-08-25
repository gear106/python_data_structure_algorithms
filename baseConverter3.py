# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:20:10 2018

@author: GEAR
"""
# 采用栈帧实现递归

from Stack import *

rStack = Stack()

def toStr(n, base):
    convert = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            rStack.push(convert[n])
        else:
            rStack.push(convert[n % base])
        n = n // base
    res = ''
    #  not后面的表达式为False的时候，执行冒号后面的语句
    while not rStack.is_empty(): # 当栈不为空时
        res += str(rStack.pop())
    return res

print(toStr(10,16))