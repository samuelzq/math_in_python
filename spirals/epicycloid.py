"""
epicycloid
通过一个动画程序演示圆外下摆线。

假设有一个定圆半径a，若有另一个半径是b的圆在上滚动，
则外圆圆周上的一定点在滚动时划出的轨迹就是一条外摆线。
在以定圆中心为原点的直角坐标系中，其方程为
x = (a+b)cosθ-bcos[(a+b)θ/b]；
y = (a+b)sinθ-bsin[(a+b)θ/b]；
"""

import turtle
import math

# 修改以下参数可以得到不同的摆线
r_big = 210
r_small = r_big / 2
d = r_small * 1

# 设置画布大小
screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("圆外下摆线")
screen.tracer(0,0)

# 创建绘制小圆的海龟
turtle.speed(0)
turtle.hideturtle()
turtle.up()
turtle.pensize(2)

# 创建绘制摆线的海龟
tt = turtle.Turtle()
tt.hideturtle()
tt.speed(0)
tt.up()
tt.pensize(1)
tt.color('red')
first = True

# 创建绘制大圆的海龟，并绘制大圆
t3 = turtle.Turtle()
t3.hideturtle()
t3.speed(0)
t3.pensize(2)
t3.up()
t3.seth(0)
t3.goto(0,-r_big)
t3.down()
t3.circle(r_big,steps=200)

# 绘制一帧图像
def draw_circle(x,y,angle):
    """ draw_circle
    ---------------------
    x, y 小圆圆心坐标
    angle 海龟的朝向
    """
    global first

    # 开始绘制外部的小圆
    turtle.clear()
    turtle.up()
    turtle.seth(0)
    turtle.goto(x, y-r_small)
    turtle.down()
    turtle.color('black')
    turtle.circle(r_small, steps=200)

    # 圆心处打点
    turtle.up()
    turtle.goto(x, y)
    turtle.dot(10, 'blue')
    turtle.down()

    # 移动到外圆上的定点
    turtle.seth(angle)
    turtle.color('purple')
    turtle.bk(d)
    turtle.dot(10,'red')

    # 连接摆线
    tt.goto(turtle.xcor(),turtle.ycor())
    if first:
        tt.down()
        first = False

# 小圆转过的弧度
angle = 0
dist = r_small*angle*math.pi/180
# 大圆上小圆经过的弧度
big_radian = dist/r_big
x = (r_big+r_small)*math.cos(big_radian)
y = (r_big+r_small)*math.sin(big_radian)
draw_circle(x,y,angle+big_radian*180/math.pi)

# 不断刷新画布上的图案，以形成动画效果
while True:
    # 小圆转过的弧度
    angle += 6
    dist = r_small*angle*math.pi/180
    # 大圆上小圆经过的弧度
    big_radian = dist/r_big
    
    # 小圆圆心坐标
    x = (r_big+r_small)*math.cos(big_radian)
    y = (r_big+r_small)*math.sin(big_radian)
    draw_circle(x,y,angle+big_radian*180/math.pi)
    if angle % 360 == 0 and int(round(big_radian*180/math.pi)) % 360 == 0:
        break
    turtle.update()
    
turtle.clear()
t3.clear()
turtle.update()
