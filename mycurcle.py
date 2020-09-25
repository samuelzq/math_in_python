from turtle import *

myturtles = []

"""
创建8个海龟克隆体，并使其来到给自的画圆起始位置。
"""
def circle_init(xc, yc, r):

    ht()
    pu()
    xa = []
    ya = []
    xa.append(xc)
    ya.append(yc + r)
    xa.append(xc)
    ya.append(yc + r)
    xa.append(xc - r)
    ya.append(yc)
    xa.append(xc - r)
    ya.append(yc)
    xa.append(xc)
    ya.append(yc - r)
    xa.append(xc)
    ya.append(yc - r)
    xa.append(xc + r)
    ya.append(yc)
    xa.append(xc + r)
    ya.append(yc)

    # 清空海龟列表
    while (len(myturtles) > 0):
        ct = myturtles.pop()
        ct.ht()
    pu()

    # 创建新的海龟克隆体，并将其添加入列表中
    for i in range(8):
        ct = clone()
        ct.pu()
        ct.speed(0)
        ct.setpos(xa[i], ya[i])
        myturtles.append(ct)

"""
使8个海龟克隆体分别移动到下一个位点。
"""
def circle_plot2(xc, yc, x, y):
    nx = []
    ny = []

    # 按反时针方向，将下一个点的坐标添加到列表中
    nx.append(xc + x)
    ny.append(yc + y)
    nx.append(xc - x)
    ny.append(yc + y)
    nx.append(xc - y)
    ny.append(yc + x)
    nx.append(xc - y)
    ny.append(yc - x)    
    nx.append(xc - x)
    ny.append(yc - y)
    nx.append(xc + x)
    ny.append(yc - y)
    nx.append(xc + y)
    ny.append(yc - x)
    nx.append(xc + y)
    ny.append(yc + x)

    # 依次使得每一个海龟克隆体移动到下一个点位
    for i in range(8):     
        myturtles[i].pd()
        myturtles[i]._tracer(0, 0)
        myturtles[i].goto(nx[i], ny[i])
        myturtles[i].up()

"""
在每一个位置上打点。
"""
def circle_plot(xc, yc, x, y):
    tracer(0, 0)
    pu()
    goto(xc + x, yc + y)
    pd()
    dot()
    pu()
    goto(xc - x, yc + y)
    pd()
    dot()
    pu()
    goto(xc - y, yc + x)
    pd()
    dot()
    pu()
    goto(xc - y, yc - x)
    pd()
    dot()
    pu()
    goto(xc - x, yc - y)
    pd()
    dot()
    pu()
    goto(xc + x, yc - y)
    pd()
    dot()
    pu()
    goto(xc + y, yc - x)
    pd()
    dot()
    pu()
    goto(xc + y, yc + x)
    pd()
    dot()
    pu()

"""
中点画圆。
"""
def my_circle(xc, yc, r):
    circle_init(xc, yc, r)

    x = 0
    y = r
    d = 1.25 - r

    circle_plot(xc, yc, x, y)

    while (x < y):
        if (d < 0):
            d = d + 2 * x + 3
        else :
            d = d + 2 * ( x - y ) + 5
            y = y - 1
        x = x + 1
        circle_plot(xc , yc , x , y)

"""
bresenham中点画圆。
"""
def my_circle_bresenham(xc, yc, r):
    circle_init(xc, yc, r)

    x = 0
    y = r
    d = 3 - 2 * r

    circle_plot(xc, yc, x, y)

    while (x < y):
        if (d < 0):
            d = d + 4 * x + 6
        else :
            d = d + 4 * ( x - y ) + 10
            y = y - 1
        x = x + 1
        circle_plot(xc , yc , x , y)
