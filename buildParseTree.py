# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 18:02:43 2018

@author: GEAR
"""

from Stack import *
from NodeBinaryTree import *
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()  #这里表达式中间要加空格
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
def postordereval(tree):
    '''
    采用后序遍历计算分析树
    '''
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()
        
def printexp(tree):
    '''
    采用中序遍历打印出树的结构
    '''
    sVal = ''
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal += str(tree.getRootVal())
        sVal += printexp(tree.getRightChild()) + ')'
    return sVal


pt = buildParseTree('( ( 10 + 5 ) * 3 )')
print(printexp(pt))
print(evaluate(pt))  # 正确输出结果应为45
print(postordereval(pt))





    