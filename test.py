from Stack import *
from NodeBinaryTree import *
import operator

def buildParseTree(pstring):
    plist = pstring.split()
    pstack = Stack()
    eTree = BinaryTree('')
    pstack.push(eTree)
    currentTree = eTree
    
    for i in plist:
        if i == '(':
            currentTree.insertLeft('')
            pstack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pstack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pstack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pstack.pop()
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
    
            
    
