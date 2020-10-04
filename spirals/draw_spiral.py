"""
Draw some spirals
"""

from turtle import *
from math import *

t = Turtle()
t.color("blue")
t.down()
a = 0
b = 5

def get_radian():
    return pi / 20 

def archimedian_spiral(a, b, t):
    """ Draw Archimedian spirals
        r = a + b*theata
    """
    t.pd()
    for i in range(200):
        theata = i * get_radian()
        x = (a + b * theata) * cos(theata)
        y = (a + b * theata) * sin(theata)
        t.goto(x, y)
    t.up()

def fermat_spiral(a, t):
    """ Draw Fermat spirals
        r^2 = a^2 * theata
    """
    global scale
    t.ht()
    t.pd()
    tt = Turtle()
    tt.ht()
    tt.pd()
    tt.color('red')
    tt.seth(180)
    for i in range(300):
        theata = i * get_radian()
        r = sqrt(a**2*theata)
        x = r * cos(theata)
        y = r * sin(theata)
        t.goto(x, y)
        tt.goto(-x, -y)
    t.up()
    t.home()
    t.fd(a + 10)
    t.seth(90)
    t.pensize(2)
    t.color('purple')
    t.pd()
    t.circle(30)

def hyperbolic_spiral(c, t):
    """Hyperbolic spiral
    双曲螺线（Hyperbolic spiral）又称倒数螺线（reciprocal spiral）
    r = c / theata
    """
    first = True
    t.up()
    for i in range(1, 720):
        theata = i * get_radian()
        r = c / theata
        x = r * cos(theata)
        y = r * sin(theata)
        t.goto(x, y)
        if first == True:
            t.pd()
        first = False

def equiangular_spiral(a, b, t):
    """equiangular spiral
    等角螺线、对数螺线或生长螺线
    r = a*e^(b*theata)
    """    
    t.pd()
    for i in range(1, 350):
        theata = i * get_radian()
        r = a * (e**(b*theata))
        x = r * cos(theata)
        y = r * sin(theata)
        goto(x, y)
    t.up()

def circle_spiral(r, n, t):
    """Circle spiral
    x = cos(theata)+(1/n)cos(n*theata)
    y = sin(theata)-(1/n)sin(n*theata)
    """
    first = True
    t.up()
    i = 1
    while True:
        theata = i * get_radian() / 10
        i += 1
        x = r * (cos(theata)+(1/n)*cos(n*theata))
        y = r * (sin(theata)-(1/n)*sin(n*theata))
        t.goto(x, y)
        if first == True:
            t.pd()
            first = False
            s = ([round(x, 5), round(y, 5)])
        else:
            if s == [round(x, 5), round(y, 5)]:
                break
    t.up()

def epicycloid(r, n, t):
    """External circle spiral
    x = cos(theata)+(1/n)*cos(n*theata)
    y = sin(theata)+(1/n)*sin(n*theata)
    """
    first = True
    t.up()
    i = 1
    while True:
        theata = i * get_radian() / 10
        i += 1
        x = r * (cos(theata)+(1/n)*cos(n*theata))
        y = r * (sin(theata)+(1/n)*sin(n*theata))
        t.goto(x, y)
        if first == True:
            t.pd()
            first = False
            s = ([round(x, 5), round(y, 5)])
        else:
            if s == [round(x, 5), round(y, 5)]:
                break
    t.up()

t.home()
t.clear()
equiangular_spiral(10, 0.1, t)
