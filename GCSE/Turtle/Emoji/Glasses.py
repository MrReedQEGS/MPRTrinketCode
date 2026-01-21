#Google "python turtle trinket"
import turtle
bob = turtle.Turtle() #make a turtle
bob.shape("turtle")
bob.speed(0)

#face
bob.penup()
bob.goto(0,-100)
bob.pendown()
bob.fillcolor(208, 222, 11)  #rgb colour picker
bob.begin_fill()
bob.circle(100)
bob.end_fill()

#eye 1
bob.penup()
bob.goto(30,30)
bob.pendown()
bob.fillcolor("white")  
bob.begin_fill()
bob.circle(15)
bob.end_fill()

bob.penup()
bob.goto(30,30)
bob.pendown()
bob.fillcolor("black")  
bob.begin_fill()
bob.circle(5)
bob.end_fill()

#eye 2
bob.penup()
bob.goto(-30,30)
bob.pendown()
bob.fillcolor("white")  
bob.begin_fill()
bob.circle(15)
bob.end_fill()

bob.penup()
bob.goto(-30,30)
bob.pendown()
bob.fillcolor("black")  
bob.begin_fill()
bob.circle(5)
bob.end_fill()

#glasses

bob.penup()
bob.goto(-30,20)
bob.pendown()
bob.circle(25)

bob.penup()
bob.goto(30,20)
bob.pendown()
bob.circle(25)

#glasses middle line
bob.penup()
bob.goto(-6,50)
bob.pendown()
bob.forward(11)
bob.hideturtle()

#glasses middle line
bob.penup()
bob.goto(-87,50)
bob.pendown()
bob.forward(32)
bob.hideturtle()

#glasses middle line
bob.penup()
bob.goto(56,50)
bob.pendown()
bob.forward(31)
bob.hideturtle()

#mouth
bob.penup()
bob.goto(35,-40)
bob.pendown()
bob.fillcolor("black")  
bob.begin_fill()
bob.circle(10)
bob.end_fill()
bob.hideturtle()
