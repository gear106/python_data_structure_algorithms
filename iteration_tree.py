# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 16:20:02 2018

@author: GEAR
"""

import turtle

def tree(brachLen, t):
    if brachLen > 5:
        t.forward(brachLen)
        t.right(20) #向右转动20度
        tree(brachLen-15, t)
        t.left(40)
        tree(brachLen-15, t)
        t.right(20)
        t.backward(brachLen)
        

def main():
    t = turtle.Turtle() #创建一个画笔
    myWin = turtle.Screen() #创建一个屏幕
    t.left(90) #画笔默认是向右的，左转90度画笔向上
    t.up()  #拿起笔
    t.backward(100) #将画笔向相反方向移动一段距离
    t.down() #放下笔
    t.color('green')
    tree(75, t)
    myWin.exitonclick()
    
if __name__ == '__main__':
    main()