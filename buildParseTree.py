# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 18:02:43 2018

@author: GEAR
"""

from Stack import *
from NodeBinaryTree import *

def buildParseTree(fpexp):
    fplist = fpexp.split()  #这里表达书中间要加空格
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    