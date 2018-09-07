# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 21:33:17 2018

@author: GEAR
"""

from Graph import *

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]  #这里将字母装进桶
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]   #这里加括号是因为后边要在列表里添加元素
                
    for bucket in  d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
                    
    return g
                    