# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:29:36 2018

@author: GEAR
"""

'''
插入排序：采用移位操作，通常移位操作只需要交换工作1/3的处理时间, 假设第一个元素是
排序好的，然后第二个元素和第一个元素比较，交换位置，依次类推
'''
def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        
        alist[position] = currentvalue
        

if __name__ == '__main__':
    test = [6,4,8,3,9,2]
    insertionSort(test)
    print(test)