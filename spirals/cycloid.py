"""
cycloid
---------------------------
绘制摆线
"""

from turtle import *
from math import *

# 设置画布大小
screen = Screen()
screen.setup(1000,1000)
screen.title("摆线")
screen.tracer(0,0)

radius = 50
ht()

# 创建绘制水平线的海龟
t = Turtle()
t.up()
t.hideturtle()
t.pensize(4)
t.goto(-500, -102)
t.pd()
t.goto(500, -102)
t.speed(0)

# 创建绘制摆线的海龟
t1 = Turtle()
t1.up()
t1.ht()
t1.speed(0)
t1.pensize(2)
t1.color('red')
first = True

def draw_circle(x, y, angle):
    """draw_circle
    --------------------------------
    绘制一帧图案
    [x, y]当前圆的位置，在此位置左侧画圆
    anlge圆转过的弧度
    """
    global first

    # 清掉上一帧的圆，在新位置重新画圆
    clear()
    up()
    goto(x, y)
    color('black')
    pd()
    circle(50)
    up()

    # 在圆心处打点
    goto(x, y + 50)
    dot(10, 'blue')

    # 移动到圆上定点
    xc = 50 * (angle - sin(angle)) + (-500)
    yc = 50 * (1 - cos(angle)) - 100
    color('purple')
    down()
    goto(xc, yc)
    dot(10, 'red')

    # 延长摆线
    t1.goto(xc, yc)
    if first:
        t1.down()
        first = False

x = -500
scale = 0.01
a = 0
radius = 50
while (x < 500):
    x += scale * radius;
    a += scale
    draw_circle(x, -100, a)
    update()
