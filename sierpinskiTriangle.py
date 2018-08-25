# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:03:12 2018

@author: GEAR
"""
# 采用递归函数画谢尔滨斯三角形
import turtle

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])   #将画笔移动到坐标为x,y的位置
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])   
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()
    
def getMid(p1, p2): #获取线段中点的坐标
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white','yellow', 
                'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], 
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                    degree-1, myTurtle)
    
        sierpinski([points[1], 
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                    degree-1, myTurtle)

        sierpinski([points[2], 
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                    degree-1, myTurtle)
    
def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoint = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(myPoint, 3, myTurtle)
    myWin.exitonclick()
    
if __name__ == '__main__':
    main()