# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:03:02 2018

@author: GEAR
"""
'''
选择排序:每次寻找n个元素中最大的一个元素并将其放到正确的位置，下一次在n-1个
元素中寻找，以此类推
'''
def selectionSort(alist):
    for num in range(len(alist)-1, 0, -1):
        indexOfMax = 0  #假设最大元素为列表初始位置元素
        for index in range(1, num+1):
            if alist[index] > alist[indexOfMax]:  # 若当前位置元素大于最大元素
                indexOfMax = index
        # 每次循环将最后一个位置元素与最大元素交换，循环元素个数减少一位
        alist[indexOfMax], alist[num] = alist[num], alist[indexOfMax] 
        
    
    
if __name__ == '__main__':
    test = [6,4,8,3,9,2]
    selectionSort(test)
    print(test)
            