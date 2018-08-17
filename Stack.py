# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 19:03:06 2018

@author: GEAR
"""

# python stack 实现

class Stack():
    #初始化栈为空列表
    def __init__(self):
        self.__items = [] 
    #判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.__items == []
    #返回栈顶元素
    def peek(self):
        return self.__items[-1]
    #返回栈的大小
    def size(self):
        return len(self.__items)
    #新元素入栈
    def push(self, item):
        self.__items.append(item)
    #栈顶元素出栈
    def pop(self):
        return self.__items.pop()
    
if __name__ == '__main__':
    #创建一个空栈对象
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.pop()
    print(myStack.size())
    print(myStack.peek())
    print(myStack.is_empty())
    
    
    