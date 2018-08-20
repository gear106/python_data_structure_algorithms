# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 18:16:24 2018

@author: GEAR
"""
#python实现Deque(双端队列)

class Deque(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
 
if __name__ == '__main__':
    s = Deque()
    s.addFront(0)
    s.addRear(1)
    print(s.items)

    