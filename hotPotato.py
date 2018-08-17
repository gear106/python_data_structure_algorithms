# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 19:47:20 2018

@author: GEAR
"""
from Queue import *

def hotPotato(namelist, num):
    simqueue = Queue()  #创建空队列
    for name in namelist:
        simqueue.enqueue(name)  #将参数全部入队列
    while simqueue.size() > 1:
        for i in range(num):
            #假设队首的人拿着东西，先将其出队再入队尾，
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue() # 在经过num次循环后将队首的元素删除
        
    return simqueue.dequeue()

print(hotPotato(['A','B','C','D'], 1))
            