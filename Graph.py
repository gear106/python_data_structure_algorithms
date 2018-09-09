# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:42:05 2018

@author: GEAR
"""

'''
图数据结构：
实现邻接表
'''

class Vertex(object):
    def __init__(self, key, color='white', distance=0, predvert=None):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.predvert = None
        
        
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    def getColor(self):
        return self.color
    
    def setColor(self, new):
        self.color = new
        
    def getDistance(self):
        return self.distance
    
    def setDistance(self, new):
        self.distance = new
        
    def getPred(self):
        return self.predvert
    
    def setPred(self, key):
        self.predvert = key
        
        
        
class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())   #用来生成迭代器
    
    
if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
        
    g.vertList
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    
    for v in g:
        for w in v.getConnections():
            print('(%s, %s)'%(v.getId(), w.getId()))
            
    print(g.getVertex(0))
    print(g.getVertices())
            
        
            
        
        
        
        
        