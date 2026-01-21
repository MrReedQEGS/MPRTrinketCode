#Theo - Year 10

import turtle, random, time

rotation = 0


bob = turtle.Turtle()

listOfRands = []

for i in range(3000):
  listOfRands.append(random.randrange(1,5))


while True:
  bob.tracer(0)
  bob.fillcolor(100,100,100)
  bob.write(" " * 100,font = ("Arial",10,"normal"))
  bob.up()
  bob.width(1)
  
  bob.goto(-0,-30)
  bob.setheading(268 + rotation)
  bob.down()
  bob.fd(100)
  bob.begin_fill()
  
  for i in range(184):
    bob.fd(1)
    bob.lt(1)
  bob.fd(100)
  for i in range(87):
    bob.fd(0.6)
    bob.lt(1.05)
  bob.setheading(180 + rotation)
  bob.fd(10)
  pos = bob.pos()
  bob.fd(30)
  for i in range(87):
    bob.fd(0.6)
    bob.lt(1.05)
  bob.up()
  bob.end_fill()
  bob.fillcolor("black")
  bob.goto(pos)
  bob.begin_fill()
  bob.down()
  bob.setheading(270 + rotation)
  bob.fd(75)
  for i in range(180):
    bob.rt(1)
    bob.fd(0.15)
  bob.fd(55)
  bob.fd(20)
  bob.up()
  bob.end_fill()
  bob.bk(110)
  bob.setheading(30 + rotation)
  bob.down()
  bob.fillcolor("white")
  bob.begin_fill()
  for i in range(36):
    bob.fd(3)
    bob.rt(10)
  bob.end_fill()
  bob.up()
  bob.setheading(0 + rotation)
  bob.bk(4)
  bob.setheading(90 + rotation)
  bob.bk(20)
  bob.fillcolor("black")
  for i in range(rotation % 360):
    bob.fd(0.3)
    bob.rt(1)
  bob.write("hp",font = ("Arial Black",16,"normal"))
  bob.setheading(90 + rotation)
  bob.up()
  bob.goto(pos)
  bob.color("grey")
  bob.fillcolor(150,150,150)
  bob.bk(20)
  bob.lt(90)
  bob.fd(5)
  bob.rt(90)
  bob.down()
  bob.begin_fill()
  bob.bk(30)
  for i in range(18):
    bob.bk(0.7)
    bob.rt(10)
  bob.bk(30)
  for i in range(18):
    bob.bk(0.7)
    bob.rt(10)
  bob.end_fill()
  bob.color(50,50,50)
  for i in range(10):
    bob.bk(3)
    bob.lt(90)
    bob.fd(7)
    bob.bk(7)
    bob.rt(90)
  bob.up()
  bob.goto(pos)
  bob.lt(90)
  bob.fd(10)
  bob.rt(90)
  
  bob.width(5)
  bob.up()
  bob.bk(180)
  bob.setheading(0 + rotation)
  bob.down()
  bob.color(200,200,200)
  for i in range(76):
    bob.fd(1)
    bob.lt(1.2)
  bob.fd(50)
  
  bob.up()
  bob.goto(pos)
  bob.lt(90)
  bob.fd(8)
  bob.rt(90)
  
  bob.color(50,50,50)
  bob.width(9)
  bob.down()
  
  go = True
  num = 0

  while go == True:
    rand = listOfRands[num]
    if rand == 1 and bob.heading() < 120:
        bob.lt(15)
    elif rand == 2 and bob.heading() > 60:
        bob.rt(15)
    else:
      bob.fd(5)
      if bob.xcor() < -200 or bob.xcor() > 200 or bob.ycor() < -200 or bob.ycor() > 200:
        go = False
    num += 1
    
  bob.update()
  time.sleep(0)
  
  bob.clear()
  
  rotation += 5
