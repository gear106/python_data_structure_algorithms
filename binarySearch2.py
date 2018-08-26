# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 09:23:41 2018

@author: GEAR
"""
'''
采用二分法搜索（递归算法）列表中的某个元素是否存在
'''

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
                return binarySearch2(alist[midpoint+1:], item)   # 这里要加1，因为不包含第一个元素

            

if __name__ == '__main__':
    testlist = [1]
    print(binarySearch2(testlist, 3))