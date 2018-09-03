# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:16:12 2018

@author: GEAR
"""
'''
二叉堆的实现:
为了使我们的堆有效的工作，我们将利用二叉树的对数性质来表示我们的堆，为了保证对数性
质，我们必须保持树的平衡，平衡二叉树在根的左右子树中具有大致相同数量的节点，在我们
堆的实现中，我们通过创建一个完整二叉树来保持树的平衡。
完整二叉树的一个特点是我们可以使用单个列表来表示它，因为树是完整的，父节点（位置i处）
的左节点在2i处，右节点在2i+1处，我们可以简单的使用整除除法，假设节点在列表的位置为i,
则其父节点在i//2处
'''
class BinHeap(object):
    def __init__(self):
        self.heapList = [0]     #首元素为零是为了后边简单的整除
        self.currentSize = 0    #列表长度

    def perUp(self, i):
        '''
        找到插入位置在i处的元素在堆中的准确位置，从下而上调整位置
        '''
        while i // 2 > 0:   # i位置元素父节点存在
            if self.heapList[i] < self.heapList[i // 2]: # 若子节点小于父节点则交换位置
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2
            
    def insert(self, k):
        '''
        在堆中插入一个元素，一般先插入到列表最后一个元素，然后调整位置
        '''
        self.heapList.append(k)
        self.currentSize += 1
        self.perUp(self.currentSize)
        
    def minChild(self, i):
        '''
        找到节点i处元素的最小子节点的位置
        '''
        if i*2 + 1 > self.currentSize:  #若右子节点不存在，返回其左子节点
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2 + 1
    def perDown(self, i):
        '''
        在删除了根节点（最小元素）之后，将列表最后一个元素放到根节点位置，但此时
        破坏了堆的结构，需要将调整当前根节点的位置到其正确的位置。从上而下调整位置
        '''
        while (i*2) <= self.currentSize:    #若当前左子节点位置小于列表总长度
            mc = self.minChild(i)   # 返回当前节点的最小子节点位置
            if self.heapList[i] > self.heapList[mc]: #r若当前节点元素大于其最小子节点
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
                
            i = mc #跳到下一子节点
            
    def delMin(self):
        '''
        删除堆中的最小元素，即根节点元素
        '''
        retVal = self.heapList[1]    #根节点元素
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.perDown(1)
        return retVal
    
    def buildHeap(self, alist):
        '''
        将一个单列表转化为堆，若采用一个节点插入的方法，时间复杂度为nlog(n)
        '''
        i = len(alist) // 2 #从中间元素开始调整元素位置，时间复杂度：O(n)
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perDown(i)
            i = i - 1
            
        
if __name__ == '__main__':
    bh = BinHeap()
    bh.buildHeap([9,5,6,2,3])
    print(bh.heapList)
    print(bh.delMin())
    print(bh.heapList)
    

    
    
        
                
                
