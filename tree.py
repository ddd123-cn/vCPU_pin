# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from turtle import *
from random import *
from math import *

def tree(n, l):
    pendown()
    t = cos(radians(heading() + 45)) /8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n*0.8, n*0.8)
        circle(3)
        left(90)
        if (random() > 0.7):
            penup()
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            
            pendown()
            right(90)
            n = cos(radians(heading() - 45)) /4 + 0.5
            pencolor(n*0.5 + 0.5, 0.4+n*0.4, 0.4+n*0.4)
            circle(2)
            left(90)
            penup()
            
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
    penup()
    backward(l)

bgcolor(0.5, 0.5, 0.5)
hideturtle()
speed(0)
tracer(400, 0)
penup()
backward(100)
left(90)
penup()
backward(300)
tree(11, 100)
done()