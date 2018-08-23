# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:29:52 2018

@author: GEAR
"""

def listSum1(num_list):  # 采用循环迭代求和
    theSum = 0
    for item in num_list:
        theSum += item
    return theSum

def listSum2(num_list):
    if (len(num_list)) == 1:
        return num_list[0]
    else:
        return num_list[0] + listSum2(num_list[1:])
    
if __name__ == '__main__':
    a = [1,2,3]
    print(listSum1(a))
    print(listSum2(a))
    
    