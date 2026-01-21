#Changing the size of the drawing window and the background colour.
#
#You will need to do "full screen" and zoom out to see the full image.  :)

import turtle
bob = turtle.Turtle()

theScreen = turtle.Screen()
theScreen.setup(width=2000,height=600)
theScreen.bgcolor(0,200,0)
bob.speed(5)
bob.penup()
bob.goto(-1000,0)
bob.pendown()
bob.forward(2000)
