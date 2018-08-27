# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:17:51 2018

@author: GEAR
"""

def quickSort(alist):
    quickSortHelpter(alist, 0 , len(alist)-1)
    
def quickSortHelpter(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelpter(alist, first, splitpoint-1)
        quickSortHelpter(alist, splitpoint+1, last)
        

def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        
        if rightmark < leftmark:
            done = True
        else:
            #alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    
    return rightmark


if __name__ == '__main__':
    test = [54,26,93,17,77,31,44,55,20]
    quickSort(test)
    print(test)