#make a turtle
import turtle
bob = turtle.Turtle()

#Do some drawing
bob.circle(70,360)

#make a font
myFont = ("Ariel",16,"normal")

#move to somewhere else
bob.penup()
bob.goto(-40,90)
bob.pendown()
bob.write("Mr Reed's",font = myFont)

bob.penup()
bob.goto(-25,70)
bob.pendown()
bob.write("circle!",font = myFont)

#get rid of turtle so we can see the text
bob.hideturtle()

