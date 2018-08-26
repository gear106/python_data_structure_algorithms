# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:57:54 2018

@author: GEAR
"""
'''
希尔排序
'''
def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print('After increment of size', sublistcount, 
              'the list is',alist)
        sublistcount = sublistcount // 2
        
def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position -= gap
        alist[position] = currentvalue
        
        
if __name__ == '__main__':
    test = [6,4,8,3,9,2]
    shellSort(test)
    print(test)
        
    