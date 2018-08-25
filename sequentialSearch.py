# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 18:14:32 2018

@author: GEAR
"""

def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


if __name__ == '__main__':
    testlsit = [1,2,4,5,6]
    print(sequentialSearch(testlsit, 7))