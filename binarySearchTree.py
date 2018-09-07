# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:17:49 2018

@author: GEAR
"""

class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self, key, val):
        '''
        创建二叉搜索树，首先检查树是否有根节点，如果没有put将创建一个新的TreeNode
        并把它作为树的根节点，作为子树的根。如果一个根节点存在，我们就调用它自己，
        进行递归，用辅助函数__put来搜索树
        '''
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    
    def __put(self, key, val, currentNode):
        '''
        搜索树：
        1.从树的根开始搜索，比较新的键值，如果新的键值小于当前节点，搜索左子树，如果
        新的键值大于当前节点，搜索右子树
        2.当无左右子树的搜索，我们发现的位置就是应该在子树中安装新节点的位置。
        3.向树中添加一个节点，在上一步发现插入对象的位置创建一个新的TreeNode。
        '''
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self.__put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self.__put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                
    def __setitem__(self, k, v):
        self.put(k,v)
        
        
    def get(self, key):
        if self.root:
            res = self.__get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    
    def __get(self, key, currentNode):
        '''
        注意使用__get方法返回一个TreeNode给get
        '''
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self.__get(key, currentNode.leftChild)
        else:
            return self.__get(key, currentNode.rightChild)
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        '''
        使用get,我们可以通过BinarySearchTree写一个__contains__方法来实现in操作
        __contains__方法将简单的调用get并在get返回值式返回True,如果返回值为None
        则返回False
        '''
        if self.__get(self, key):
            return True
        else:
            return False
        
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self.__get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in Tree')
    
    def __delitem__(self, key):
        self.delete(key)
        
    
    def spliceOut(self):
        '''
        删除后继节点，并重新排序
        '''
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
                
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    def findMin(self):
        current = self
        while
                    
            
    
class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        
    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
            

        

        
    
            