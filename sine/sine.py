# -*- coding: UTF-8 -*-
"""
sine.py
一个绘制正弦曲线的动画程序。
用以说明，正弦曲线和单位圆上一点位置的关系。
"""

import turtle
import math

xstart = -50
radius = 180

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("Sine Wave")
screen.tracer(0,0)

# 绘制x、y轴
turtle.up()
turtle.hideturtle()
turtle.speed(0)
turtle.goto(-500, 0)
turtle.pd()
turtle.goto(500, 0)
turtle.up()
turtle.goto(0, -500)
turtle.pd()
turtle.goto(0, 500)

# 创建绘制正弦曲线的海龟
t = turtle.Turtle()
t.pu()
t.home()
t.pensize(2)
t.color('green')

# 创建绘制圆的海龟
t2 = turtle.Turtle()
t2.up()
t2.ht()
t2.speed(3)
t2.setx(-50)
t2.seth(90)
t2.pensize(2)
t2.color('blue')

# 创建海龟以绘制创建三条连接线：
# 圆心和动点、动点和正弦曲线前端
t3 = turtle.Turtle()
t3.up()
t3.ht()
t3.speed(0)
t3.color('red')

def draw_wave(angle):
    """draw_wave
    绘制每一帧图像
    """
    global xstart, radius

    # 清除上一帧图像
    t3.clear()
    t.clear()
    t.home()
    t.ht()
    t2.clear()

    # 绘制动点在圆上的运动轨迹
    t2.pu()
    t2.goto(xstart, 0)
    t2.seth(90)
    t2.pd()
    t2.circle(radius, angle)
    
    t3.up()
    # 绘制圆心点并将圆心和动点连接
    t3.goto(xstart-radius, 0)
    t3.pd()
    t3.dot(8, 'red')    
    t3.pencolor('red')
    t3.goto(t2.pos())

    # 从动点向x轴做垂线，
    t3.up()
    t3.goto(t2.xcor(), 0)
    t3.pd()
    t3.dot(8, 'red')
    t3.pencolor('purple')
    t3.goto(t2.pos())
    t3.dot(8, 'blue')

    # 绘制正弦曲线
    i = 0    
    t.pd()
    while (i <= angle):
        r_tange = i / 180 * math.pi
        t.goto(i, radius * math.sin(r_tange))
        i += 0.5        
    t.pu()

    # 并连接动点和正弦曲线前端    
    t3.pencolor('brown')
    t3.goto(t.pos())
    t3.dot(8, 'blue')

t3.pensize(2)
a = 0
while (a <= 360):
    draw_wave(a)
    a += 0.5
    turtle.update()

turtle.update()
