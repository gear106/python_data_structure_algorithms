# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:09:22 2018

@author: GEAR
"""

from Graph import *

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        
        
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex.getColor() == 'white':
            self.dfavisit(aVertex)
            
    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setColo