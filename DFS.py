# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:33:24 2018

@author: GEAR
"""
from Graph import*

def knightGraph(bdSize):
    ktGraph = Graph() 
    # 遍历每个格
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize) #得到当前点所有下一步的位置
            for e in newPositions:
                nid = posToNodeId(e[0],e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)  #对每一个点添加其下一步可能的位置
                
    return ktGraph

def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1,-2), (-1,2), (-2,-1),(-2,1), #表示左右上下移动的格数
                   (1,-2), (1,2), (2,-1), (2,1)]
    
    for i in moveOffsets:
        newX = x + i[0]  #取出x坐标
        newY = y + i[1]  #取出y坐标
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))  #这里添加的是tuple
    return newMoves


def legalCoord(x, bdSize):      # 判断走的位置是否在棋盘内
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    
def posToNodeId(row, col, bdSize):  # 每个点的坐标
    
    return row*bdSize + col


def knightTour(n, path, u, limit):
    '''
    n    :  搜索树当前的深度
    path :  到此位置访问的顶点的列表
    u    :  图中我们希望探索的顶点
    limit： 路径中的节点总数
    '''
    u.setColor('gray')
    path.append(u)  # 当前顶点加入路径
    if n < limit:
        nbrList = list(u.getConnections()) # 对所有合法移动逐一深入
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':  # 选择白色未经过的点深入
                done = knightTour(n+1, path, nbrList[i], limit) #层次加一，递归深入
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
        else:
            done = True
    return done


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
                resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]

                
    
        