import turtle
import os

# set up screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('space invaders')


# draw border
border_pen = turtle.Turtle()
border_pen.speed(2)
border_pen.color('green')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# https://www.youtube.com/watch?v=FdmjXnyoS0A






delay = input('press enter to finish')
