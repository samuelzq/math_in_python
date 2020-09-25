from turtle import *

def polygon(side = 3, r = 100):
    setheading(90)
    pu()
    for i in range(side):
        fd(r)
        loc1 = pos()
        bk(r)
        left(360 / side)
        fd(r)
        pd()
        loc2 = pos()
        goto(loc1)
        loc1 = loc2
        pu()
        setpos(0, 0)

polygon()
        
