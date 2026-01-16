import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t = turtle.Turtle()
t.speed(0)

for i in range(360):
    t.pencolor(random.choice(colors))
    t.forward(i/6)
    t.left(10)
    t.width(i/50)  # ticker line effect

turtle.done()
