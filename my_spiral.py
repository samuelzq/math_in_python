'''
my_spiral.py
---------------------
本程序用来演示螺旋线。

悬臂个数等于悬臂上螺旋线的边数。每条边的颜色会交替变换。
'''

from turtle import *

t = Turtle()
t.speed(10)
t.penup()
wn = Screen()
wn.bgcolor("black")

# 用户输入螺旋的边数, 默认4, 最小2, 最大6
sides = int(input("How many sides in your spiral of spirals? (2-6)"))

# 每条边的候选色彩
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

def spiral(sides, r, tt):
    "绘制螺旋线"
    global colors
    tt.pd()    
    for i in range(1, sides+1):
        n = (i - 1) % r
        # 换颜色
        tt.color(colors[n])
        tt.fd(2*i)
        tt.rt(360 / r - 2)
    tt.up()

# 绘制大螺旋
for m in range(100):
    heading = t.heading()   # 海龟当前指向
    t.forward(m*4)
    
    # 开始在指定位置绘制螺旋线
    spiral(int(m/2), sides,  t)

    # 恢复海龟初始位置和指向
    t.home()
    t.setheading(heading)

    # 指向下一个位置
    t.left(360/sides + 2)
