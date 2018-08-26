# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 13:04:40 2018

@author: GEAR
"""
'''
冒泡通常被认为是最低效的排序算法，因为它必须在最终位置被知道之前交换，但其遍历列表
的整个未被排序的部分，它可以做其他排序算法不能做的事，比如如果在遍历时发现没有元素
交换，则可以提前终止排序，冒泡排序具有识别排序列表和停止的优点，通常称之为短冒泡排序
'''
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
                
        passnum -= 1


if __name__ == '__main__':
    test = [2,3,4,5,8,7,1]
    shortBubbleSort(test)
    print(test)
    
                
