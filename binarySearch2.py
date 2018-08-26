# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 09:23:41 2018

@author: GEAR
"""

def binarySearch2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if item == alist[midpoint]:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch2(alist[:midpoint], item)
            else:
                return binarySearch2(alist[midpoint+1:], item)

            

if __name__ == '__main__':
    testlist = [1]
    print(binarySearch2(testlist, 3))