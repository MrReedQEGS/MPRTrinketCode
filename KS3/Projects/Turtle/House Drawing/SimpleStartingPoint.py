import turtle
bob = turtle.Turtle()

#Draw the house
bob.fillcolor(55, 219, 208) #rgb colour picker
bob.begin_fill()
bob.goto(0,0)
bob.goto(100,0)
bob.goto(100,100)
bob.goto(50,150)
bob.goto(0,100)
bob.goto(0,0)
bob.end_fill()

#Move
bob.penup()
bob.goto(10,10)
bob.pendown()

#Draw one window
bob.fillcolor("yellow")
bob.begin_fill()
for i in range(4):
  bob.forward(15)
  bob.left(90)
bob.end_fill()

bob.hideturtle()

