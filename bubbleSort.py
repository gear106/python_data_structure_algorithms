# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 11:58:26 2018

@author: GEAR
"""
'''
冒泡排序实现
'''
def bubbleSort(alist):
    for num in range(len(alist)-1, 0, -1):  #从最大的位置开始依次减小
        for i in range(num):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
#                a[i], a[j] = a[j], a[i]     #等价于上述三行的交换方法，python支持同时交换


if __name__ == '__main__':
    test = [5,6,3,7,2]
    bubbleSort(test)
    print(test)