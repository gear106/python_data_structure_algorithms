# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 09:31:30 2018

@author: GEAR
"""

from Graph import *
from Queue import *
from alphabet_graph import *

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)   #父顶点
    
    vertQueue = Queue()
    vertQueue.enqueue(start)    #向队尾插入新元素
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()   #将队首元素移出队列
        for nbr in currentVert.getConnections(): # nbr表示父顶点所连接的子顶点
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
        
        
def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())
    
wordGraph = buildGraph('wordFile.txt')
bfs(wordGraph, wordGraph.getVertex('FOOL'))
traverse(wordGraph.getVertex('SAGE'))



        