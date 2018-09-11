# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:01:00 2018

@author: GEAR
"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
class UnorderedList(object):
    def __init__(self):
        self.head = None
        
    def Empty(self):
        '''
        判断链表是否为空
        '''
        return self.head == None
    
    def prepend(self, val):
        '''
        在链表头部插入一个元素
        '''
        temp = ListNode(val)
        temp.next = self.head
        self.head = temp
        
    def pop_first(self):
        '''
        删除表头节点并返回这个元素
        '''
        if self.Empty():
            print('链表为空')
            return
        else:
            val = self.head.val
            self.head = self.head.next
            return val
    def append(self, val):
        '''
        在链表尾部插入一个元素
        '''
        temp = ListNode(val)
        if self.Empty():
            self.head = temp
            
        current = self.head
        while current.next != None:
            current = current.next
        current.next = temp
    def pop_last(self):
        '''
        删除链表尾部的元素
        '''
        # 链表为空时
        if self.Empty():
            print('链表为空')
            return
        # 只有一个元素时
        current = self.head
        if current.next is None:
            e = current.val
            self.head = None
            return e
        # 有一个以上元素时
        while current.next.next != None:
            current = current.next
        e = current.next.val
        current.next = None
        return e
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
            
    def search(self, val):
        current = self.head
        found = False
        while current != None and not found:
            if current.val == val:
                found = True
            else:
                current = current.next
        return found
    
    def remove(self, val):
        previous = None
        current = self.head
        found = False
        while current != None and not found:
            if current.val == val:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = self.head.next
#            self.head = current.next   #等价
        else:
            previous.next = current.next
#            previous.next = previous.next.next  #等价
        
    
    def printList(self):
        '''
        打印出链表
        '''
        if self.Empty():
            print('\nlist\'s length is 0')
        else:
            current = self.head
            print('Head -->', current.val, end=' ')
            while current.next != None:
                current = current.next
                print('-->', current.val, end=' ')
            print('--> None')
            
    def removeAll(self, val):
        '''
        移除链表中所有值为val的元素
        '''
        current = self.head
        if current.val == val:
            self.head = current.next
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
    def reverse(self):
        '''
        将链表首尾元素反转
        '''
        prev = None
        while self.head.next is not None:
            nxt = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = nxt
        self.head.next = prev
                
    
if __name__ == '__main__':
    s1 = UnorderedList()
    s1.prepend(3)
    s1.prepend(4)
    s1.prepend(5)
    s1.prepend(6)
    s1.prepend(4)
    s1.append(4)
    s1.printList()
    s2 = s1.removeAll(4)
    s1.printList()
    s1.reverse()
    s1.printList()