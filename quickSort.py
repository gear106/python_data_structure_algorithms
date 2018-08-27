# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:17:51 2018

@author: GEAR
"""

def quickSort1(alist):
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

def quickSort2(alist, first, last):
    leftmark = first    # 左起始点
    rightmark = last   # 右起始点
    
    if leftmark >= rightmark:   # 结束排序
        return
    pivotvalue = alist[leftmark]  # 首元素
    # 一次排序， leftmark和rightmark的值不断靠近， 然后停止，结束一次排序
    while leftmark < rightmark:
        # 和最右边的比较， 如果最右值 >= pivotvalue, 最右值位置-1，如果小于就交换位置
        while leftmark < rightmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        alist[leftmark] = alist[rightmark]
        
        # 和最左值比较， 如果最左值 <= pivotvalue, 最左值位置+1， 如果大于就交换位置
        while leftmark < rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        alist[rightmark] = alist[leftmark]
        
    alist[leftmark] = pivotvalue
    
    #左边排序
    quickSort2(alist, first, leftmark-1)
    #右边排序
    quickSort2(alist, leftmark+1, last)
    
    


if __name__ == '__main__':
    test = [54,26,93,17,77,31,44,55,20]
    quickSort2(test, 0 , len(test)-1)
    print(test)