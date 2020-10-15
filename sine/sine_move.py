# -*- coding: UTF-8 -*-

import turtle
import math
from time import sleep

radius = 800
ter = False
screen = turtle.Screen()
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.title("正弦运动")

t = turtle.Turtle('circle')
t.up()
t.speed('slow')
t.shapesize(1)

t2 = turtle.Turtle('circle', visible=False)
t2.color("red")
t2.up()

t3 = turtle.Turtle('circle', visible=False)
t3.color("blue")
t3.up()

def draw_x():
    t.up()
    t.ht()
    t.goto(-1000, 0)
    t.pd()
    t.goto(1000,0)
    t.up()

def draw_y():
    t.up()
    t.ht()
    t.goto(0, -1000)
    t.pd()
    t.goto(0, 1000)    
    t.up()

def fxn(x, y):
    global ter
    ter = True

turtle.onscreenclick(fxn)

def vertical_move():
    global ter
    t.clear()
    t.ht()
    draw_x()
    t.home()
    t.st()
    i = 0;
    while ter == False:
        y = radius*math.sin(math.radians(i))
        i += 1
        t.goto(0, y)

def horizontal_move():
    global ter
    
    t.ht()
    t.clear()
    draw_y()
    t.home()
    t.st()
    i = 0;
    while ter == False:
        x = radius*math.sin(math.radians(i))
        i += 1
        t.goto(x, 0)        

def combined_move():
    global ter
    
    t.ht()
    t.clear()
    draw_x()
    draw_y()
    i = 0
    y = radius* math.sin(math.radians(i))
    x = radius* math.sin(math.pi/2+math.radians(i))
    i += 1
    t.ht()
    t.goto(x, y)
    t.st()
    t2.goto(0, y)
    t3.goto(x, 0)
    t2.st()
    t3.st()
    while ter == False:
        y = radius* math.sin(math.radians(i))
        x = radius* math.sin(math.pi/2+math.radians(i))
        i += 1
        t.goto(x, y)
        t2.goto(0, y)
        t3.goto(x, 0)
    t2.ht()
    t3.ht()

def compared_move():
    global ter
    t.ht()
    t.clear()
    draw_x()
    t.goto(-100, 0)
    t.st()
    t2.up()
    t2.ht()
    t2.goto(100, 0)
    t2.st()
    i = 0;
    y1 = 0
    up = True
    while ter == False:
        y = radius* math.sin(math.radians(i))
        i += 1
        t.goto(-100, y)
        if up == True:
            y1 += radius/90
            if (y1 >= radius):
                up = False
                y1 = radius
        else:
            y1 -= radius/90
            if (y1 <= -1 * radius):
                up = True
                y1 = -1*radius
        
        t2.goto(100, y1)

while(1):
    s = input("请输入你的选择（1、垂直运动；2、水平运动；3、水平+垂直；4、比较正弦和匀速运动；0、退出）： ")
    ter = False
    t2.ht()
    if s=='1':
        vertical_move()
    if s=='2':
        horizontal_move()
    if s=='3':
        combined_move()
    if s=='4':
        compared_move()
    if s=='0':
        break

print("Exit")
turtle.bye()
