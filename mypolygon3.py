from turtle import *
from math import *

def polygon(side = 3, r = 100):
    x = []
    y = []
    for i in range(side):
        a = pi/2 + 2 * pi / side * i
        x.append(r * cos(a))
        y.append(r * sin(a))
    pu()
    setpos(x[0], y[0])
    pd()
    for i in range(side - 1):
        goto(x[i + 1], y[i + 1])
    goto(x[0], y[0])
    pu()
    home()

polygon()
