from turtle import *
from random import randint

bgcolor('black')
x = 0
speed(0)
while x < 200:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    colormode(255)
    pencolor(r, g, b)
    fd(5 + x)
    rt(20.100)
    x = x + 1

exitonclick()