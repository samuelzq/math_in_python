from turtle import *

def polygon(side_num = 4, side_length = 100):
    for i in range(side_num):
        forward(side_length)
        right(360/side_num)


for i in range(20):
    polygon(4, 100 + 20 * i)
    rt(5)
