# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:14:46 2018

@author: GEAR
"""

import turtle

myTurtle  =turtle.Turtle()
myWin  = turtle.Screen()

def drawSprial(myTurtle, linelen):
    if linelen > 0:
        myTurtle.forward(linelen)
        myTurtle.right(90)
        drawSprial(myTurtle, linelen-5)

drawSprial(myTurtle, 100)
myWin.exitonclick()