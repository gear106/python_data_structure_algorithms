# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:59:12 2018

@author: GEAR
"""
'''
python实现有序列表，和无序列表不同的是，有序列表元素是有顺序的，在add和search元素
时和无序列表有所不同
'''

class Node(object): #定义节点类
    def __init__(self, item):
        self.val = item
        self.next = None
        
    def getVal(self):
        return self.val
    
    def getNext(self):
        return self.next
    
    def setVal(self, item):
        self.val = item
        
    def setNext(self, item):
        self.next = item

class OrderedList(object):  #定义有序列表类
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            current = current.getNext()
            count += 1       
        return count
    
    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while current != None and not found:
            if current.getVal() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
    def search(self, item):
        curent = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.val == item:
                found = True
            else:
                if current.getVal() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False    
        while current != None and not stop:
            if current.getVal() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            # temp指向head, head变为temp
            temp.setNext(self.head)
            self.head = temp
        else:   
            # temp指向current,precvious指向temp
            temp.setNext(current)
            previous.setNext(temp)
            
            
    def printList(self):
        '''
        print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。
        '''
        if self.isEmpty():
            print('list\'s length is 0')
        else:
            current = self.head
            print('Head -->', current.getVal(), end=' ')
            while current.getNext() != None:
                current = current.getNext()
                print('-->', current.getVal(), end=' ')
            print('--> None')
            
if __name__ == '__main__':
    s1 = OrderedList()
    s1.add(1)
    s1.add(2)
    s1.add(5)
    s1.add(3)
    s1.printList()
        
            
            
    
        
    
    