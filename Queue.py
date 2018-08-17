# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 19:28:40 2018

@author: GEAR
"""
#pyhton实现队列
class Queue():
    #初始化空队列
    def __init__(self):
        self.items = []
    #判断队列是否为空
    def is_empty(self):
        return self.items == []
    #向队尾插入一个新的元素
    def enqueue(self, item):
        self.items.insert(0, item)
    #判断队列的大小
    def size(self):
        return len(self.items)
    #将队首的元素移除队列
    def dequeue(self):
        return self.items.pop()
        
if __name__ == '__main__':
    myQueue = Queue()
    myQueue.enqueue('x')
    myQueue.enqueue('y')
    myQueue.enqueue('z')
    print(myQueue.dequeue())
    print(myQueue.size())
    print(myQueue.is_empty())
    
        
        