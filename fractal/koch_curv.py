# -*- coding: UTF-8 -*-
"""
koch_curv.py

绘制科赫曲线
"""

import turtle

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("科赫曲线")
screen.tracer(0,0)

level = 1
side  = 600

def koch(size, n, tt):
    """
    绘制一条科赫曲线

    size：边长
    n：当前阶数
    tt：绘制曲线所用的海龟
    """
    if n==0:
        tt.fd(size) #递归结束
    else:
        for angle in [0,60,-120,60]:
            tt.left(angle)
            koch(size/3, n-1, tt) #递归

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.up()
t.goto(-0.5*side, 150)
t.pd()
t.color("black", "skyblue")
t.begin_fill()
for i in range(4):
    koch(side, level, t)
    t.right(120)
t.end_fill()
screen.update()
