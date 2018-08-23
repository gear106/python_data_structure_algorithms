# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:59:31 2018

@author: GEAR
"""
'''
采用递归求解将10进制的数转化为2-16进制之间的数
'''
def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n % base]

print(to_str(10, 2))
