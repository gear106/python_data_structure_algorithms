# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 08:52:41 2018

@author: GEAR
"""
'''
采用二分法寻找列表中的元素
'''

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

if __name__ == '__main__':
    testlist = [0,1,3,4,5,6,8]
    print(binarySearch(testlist, 3))