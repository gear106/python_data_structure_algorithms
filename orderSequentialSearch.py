# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 18:23:00 2018

@author: GEAR
"""
'''
顺序搜索一个元素是否在排序列表中，若列表中的某一个元素大于这个元素
则立即停止搜索，即这个元素在列表中不存在
'''
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

if __name__ == '__main__':
    testlist = [1,2,4,5,8]
    print(orderedSequentialSearch(testlist, 3))