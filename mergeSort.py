# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:08:48 2018

@author: GEAR
"""

'''
归并排序
'''

def mergeSort(alist):
    print('splitting', alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i, j, k = 0, 0, 0 
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
            
        while i < len(lefthalf):    #排序剩下的元素
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):   #同上
            alist[k] = righthalf[j]
            j += 1
            k += 1
        print('Merging', alist)


if __name__ == '__main__':
    test = [54,26,93,17,77,31,44,55,20]
    mergeSort(test)
    print(test)
        