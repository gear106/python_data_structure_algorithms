# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:04:26 2018

@author: GEAR
"""

class BinaryTree(object):
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
        

    def insertLeft(self, newNode):
        '''
        这里需要考虑两种情况，一是发现没有左子节点，这时只需要向树中添加
        一个节点，第二种情况是树中存在左子节点，这时需要插入一个节点并将
        现有子节点放到树的下一层中去
        '''
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def insertRight(self, newNode):
        '''
        插入右子节点需要考虑对称情况，没有右子节点，或者我们在根节点和现有
        右节点之间插入节点
        '''
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    '''
    为了完成一个简单二叉树数据结构的定义，我们将实现获取左右子树以及根值的
    方法
    '''
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, val):
        self.key = val
        
    def getRootVal(self):
        return self.key
    
    
if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())
    r.insertLeft('bb')
    print(r.getLeftChild().getRootVal())
    print(r.getLeftChild().getLeftChild().getRootVal())
        
            
    
    