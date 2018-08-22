# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 18:41:33 2018

@author: GEAR
"""
# 链表实现的基本构造块是节点，每个节点至少保留两个信息，列表本身和对下一个节点的引用
class Node(object):
    def __init__(self, new):
        self.numb = new
        self.next = None
    
    def getData(self):
        return self.numb
    
    def getNext(self):
        return self.next
    
    def setData(self, new):
        self.numb = new
        
    def setNext(self, new):
        self.next = new
        
# 无序列表类
class UnorderedList(object):
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
            
    def search(self, item):
        current = self.head
        found = False
        
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    # 这里需要注意，需要添加一个临时变量(previous)记录移除前一个数链表所示的位置       
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            #这里修改previous会间接修改链表，相当于C++中的引用
            previous.setNext(current.getNext())
            
    def printList(self):
        if self.isEmpty():
            print('\nlist\'s length is 0')
        else:
            current = self.head
            print('Head -->', current.getData(), end=' ')
            while current.getNext() != None:
                current = current.getNext()
                print('-->', current.getData(), end=' ')
            print('--> None')
            
        
                
            
    
if __name__ == '__main__':
    myList = UnorderedList()
    myList.add(1)
    myList.add(2)
    myList.add(5)
    myList.add(3)
    print(myList.size())
    print(myList.isEmpty())
    print(myList.search(1))
    myList.printList()
    
    