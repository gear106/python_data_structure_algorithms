# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 21:39:26 2018

@author: GEAR
"""

from Stack import *

def baseConverter(decNumber, base):
    '''
    采用不断除以base(2~16)求余数的方法将十进制数转化为base进制数,将所得余数入栈，再将余数出栈
    按出栈顺序即为所求二进制数
    '''
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    binString = ""
    while not remstack.is_empty():   # 当栈不为空时
        binString += digits[remstack.pop()]
    return binString

print(baseConverter(10,16))
