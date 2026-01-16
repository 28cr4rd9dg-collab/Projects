from turtle import *
from colorsys import hsv_to_rgb

bgcolor = 'black'
speed(0)
h = 0

for i in range(200):
    h += 0.0015
    color(hsv_to_rgb(h, 1, 1))
    goto(0, 0)
    fd(i)
    circle(200, 50)
    rt(10)

hideturtle()
done()
