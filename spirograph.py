import turtle
import random

alex = turtle.Turtle()
wn = turtle.Screen()

r = 100
wn.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spirograph():
    for i in range(0, 361, 10):
        alex.speed("fastest")
        alex.setheading(i)
        alex.color(random_color())
        alex.circle(r)


spirograph()

wn.exitonclick()
