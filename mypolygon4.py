from turtle import *

def polygon(side = 3, r = 100):
    p = []
    setheading(90)
    hideturtle()
    pu()
    for i in range(side):
        fd(r)
        p.append(pos())
        bk(r)
        left(360/side)

    goto(p[0])
    showturtle()
    pd()
    for i in range(side):
        goto(p[i])
    goto(p[0])
    pu()
    home()

polygon()
