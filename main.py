import colors
import turtle
import random

color_palette = colors.color_palette

alex = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)


def random_color():
    randomcolor = random.choice(color_palette)
    return randomcolor


alex.speed('fastest')
alex.up()


def painting_maker():
    x = -255
    y = -225
    alex.setposition(x, y)
    for j in range(10):
        for i in range(10):
            alex.color(random_color())
            alex.dot(20)
            alex.forward(50)
        y += 50
        alex.setposition(x, y)
    alex.hideturtle()


painting_maker()

wn.exitonclick()
