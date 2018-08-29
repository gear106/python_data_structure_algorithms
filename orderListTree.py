# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:16:37 2018

@author: GEAR
"""
'''
树的遍历：树的遍历一般有三种方式：前序，中序， 后序
前序：首先访问根节点，然后递归地做左侧子树的前序遍历，随后是右侧子树的前序遍历
中序：递归地对左子树进行一次遍历，访问根节点，最后遍历右子树
后序：先递归地对左子树和右子树进行后序遍历，然后访问根节点
'''

def preorder(tree):
    '''
    前序遍历
    '''
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
def postorder(tree):
    '''
    后序遍历
    '''
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
        
def inorder(tree):
    '''
    中序遍历
    '''
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
        

        

        
        