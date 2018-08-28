# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:13:05 2018

@author: GEAR
"""
'''
采用嵌套列表表示树，这种方法的特点在于一旦树被构建， 这个结构本身
是递归的，子树具有一个根值和两个表示叶节点的空列表， 其容易扩展到
多叉树
待解决问题：添加bulidTree函数，通过调用嵌套列表操作函数，生成树结构
示意图
'''

def BinaryTree(root):
    '''
    简单的构造一个具有根节点和两个子列表为空的列表
    '''
    return [root, [], []]

def insertLeft(root, newBranch):
    '''
    要将左子树添加到树的根，需要在根列表的第二个位置插入一个新列表
    若根列表第二个位置已经存在元素，需要沿着其把它作为添加的列表的
    左子节点
    '''
    t = root.pop(1)     #若这里不存在子树，则为0， 存在则为子树
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
        
    return root

def insertRight(root, newBranch):
    '''
    插入右子节点，类似于插入左子节点
    '''
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
        
    return root

'''
为了完成树形函数，还需要编写一些访问函数来获取和设置根节点的值
'''

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal
    
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == '__main__':
    
    r = BinaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    
    left = getLeftChild(r)
    print('left:', left)
    
    right = getRightChild(r)
    print('right:', right)
    
    insertLeft(left, 11)
    print(r)


    

