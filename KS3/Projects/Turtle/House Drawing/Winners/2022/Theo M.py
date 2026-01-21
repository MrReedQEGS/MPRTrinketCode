import math
import turtle
import random

screen = turtle.Screen()
screen.setup(width = 650, height =  400)

bob = turtle.Turtle()
bob.shape("turtle")
bob.hideturtle()
bob.tracer(5, 0)
bob.penup()
bob.speed(0)
bob.goto (-75,-100)
bob.color(100,200,0)

#all the varibles for lengths

z = 100 #length of diagonals
a = 37 #angle of diagonals

#define functions for shape automation



def coolshape(sides,fill):
  if fill:
    bob.color(245,245,240)
    bob.begin_fill()
  else:
    bob.color(150,150,100)
  l = []
  l2 = []
  l3 = []
  l4 = []
  l5 = []
  l6 = []
  l7 = []
  l8 = []
  total = []
  length = 200 / sides * math.pi
  sidesdone = 0
  ang = (360/sides)
  ang2 = 0
  for i in range(sides):
    bob.forward(length)
    if ang2 + ang  > a and ang2 < (a+180) :
      bob.right(ang2-a)
      l2.append(bob.position())
      
      if fill == False:
        bob.forward(z/6)
        l3.append(bob.position())
        bob.forward(z/6)
        l4.append(bob.position())
        bob.forward(z/6)
        l5.append(bob.position())
        bob.forward(z/6)
        l6.append(bob.position())
        bob.forward(z/6)
        l7.append(bob.position())
        bob.forward(z/6)
        l8.append(bob.position())
      else:
        bob.fd(z)
      
      
      
      l.append(bob.position())
      
      bob.back(z)
      
      bob.right((360-(ang2+180-a))-180)
    bob.left(ang)
    ang2 += ang
  
  if fill == False:
    total.append(l3)
    total.append(l4)
    total.append(l5)
    total.append(l6)
    total.append(l7)
    total.append(l8)
  
  bob.width(1)
  
  if fill == False:
    for j in total:
      bob.up()
      bob.goto(j[0])
      bob.down()
      for i in j:
        bob.goto(i)
  
  bob.width(2)
  
  bob.up()
  
  bob.goto(l2[0])
  bob.down()
  
  for i in l:
    bob.goto(i)
  bob.setheading(a)
  bob.back(z)
  bob.setheading(0)
  bob.up()
  bob.goto(-75,-100)
  bob.down()
  if fill:
    bob.end_fill()

def cloued(sise):
  bob.width(7)
  bob.color(240,240,240)
  bob.setheading(90)
  for i in range(10):
    bob.back(sise)
    bob.left(9)
  bob.begin_fill()
  prevpos = bob.position()
  for i in range(10):
    bob.forward(sise)
    bob.right(9)
  for i in range(18):
    bob.forward(sise)
    bob.right(10)
  bob.setheading(90)
  for i in range(18):
    bob.forward(sise * 1.3)
    bob.right(10)
  bob.setheading(90)
  for i in range(18):
    bob.forward(sise * 0.8)
    bob.right(10)
  bob.setheading(90)
  for i in range(10):
    bob.back(sise)
    bob.right(9)
  bob.goto(prevpos)
  bob.end_fill()

def window():
  for i in range(4):
    bob.forward(20)
    bob.left(90)
  bob.forward(10)
  bob.left(90)
  bob.forward(20)
  bob.back(10)
  bob.left(90)
  bob.back(10)
  bob.forward(20)
  bob.left(90)
  bob.forward(10)
  bob.left(90)

def gras(x, y):
  bob.up()
  bob.goto(x,y)
  bob.down()
  bob.begin_fill()
  bob.setheading(100)
  for i in range(10):
    bob.forward(1.66)
    bob.left(1)
  for i in range(7):
    bob.back(2.66)
    bob.right(5)
  
  bob.goto(x + 2,y)
    
  for i in range(10):
    bob.forward(2.33)
    bob.right(1.33)
  for i in range(7):
    bob.back(3.33)
    bob.left(4)
  
  
  bob.goto(x + 8,y)
  
  for i in range(10):
    bob.forward(1.66)
    bob.right(5)
  for i in range(7):
    bob.back(2.66)
    bob.left(5)
    
  bob.end_fill()
  bob.up()
  bob.setheading(0)

def flower(x,y):
  bob.up()
  bob.goto(x,y)
  bob.down()
  bob.begin_fill()
  bob.color(100,200,50)
  bob.setheading(90)
  bob.forward(30)
  bob.right(90)
  bob.forward(5)
  bob.right(90)
  bob.forward(30)
  bob.right(90)
  bob.forward(5)
  bob.right(90)
  bob.end_fill()
  
  bob.goto(x,y + 30)
  bob.color(255,50,0)
  bob.begin_fill()
  for i in range(18):
    bob.forward(3)
    bob.left(20)
  bob.end_fill()
  bob.setheading(-40)
  bob.begin_fill()
  for i in range(18):
    bob.forward(3)
    bob.left(20)
  bob.end_fill()
  bob.setheading(90)
  bob.forward(5)
  bob.setheading(25)
  bob.begin_fill()
  for i in range(18):
    bob.forward(3)
    bob.left(20)
  bob.end_fill()
  bob.goto(x,y + 35)
  bob.color(0,0,0)
  bob.begin_fill()
  for i in range(18):
    bob.forward(1)
    bob.left(20)
  bob.end_fill()




# and the drawing begins!

while True:
  
  
  side = input("how many sides")
  while side.isdigit() == False:
    side = input("enter a number!")
  
  side = int(side)
  
  if side < 3:
    print("hey! thats not possible sideLengthu fool")
    exit()
  elif side > 100:
    print("100 sides is the best circle ur gonna get.")
    exit()
  
  
  color = 115
  
  bob.width(10)
  
  bob.goto(-600,-10)
  
  bob.setheading(-45)
  
  bob.down()
  
  for i in range(85):
    bob.color(color,color + 50 , color + 100)
    bob.left(90)
    bob.forward(10)
    bob.right(90)
    bob.forward(900)
    bob.back(900)
    color = color + 1
  
  bob.width(7)
  
  bob.up()
  bob.goto(-280,150)
  bob.down()
  cloued(3.5)
  
  bob.up()
  bob.goto(-70,150)
  bob.down()
  cloued(2.5)
  
  
  bob.up()
  
  bob.goto(280,210)
  bob.setheading(135)
  bob.down()
  bob.color(255,255,0)
  bob.begin_fill()
  for i in range(36):
    bob.forward(10)
    bob.left(10)
  bob.end_fill()
  bob.up()
  
  
  bob.goto(180,130)
  bob.down()
  cloued(3)
  
  bob.up()
  bob.goto(-75,-100)
  bob.down()
  
  
  bob.color(100,200,0)
  bob.width(2)
  bob.setheading(0)
  bob.up()
  bob.goto(-400,-200)
  bob.down()
  
  colour = 120
  
  bob.width(3)
  
  for i in range(60):
    bob.color(colour, colour + 100, 0)
    bob.left(90)
    bob.forward(3)
    bob.right(90)
    bob.forward(1000)
    bob.back(1000)
    colour = colour + 1
  
  bob.color(100,200,50)
  bob.width(2)
  
  x = -400
  y = -40
  
  bob.tracer(10, 0)
  
  for i in range (10):
    gras(random.randrange(x - 30, x + 30), random.randrange(y - 30, y + 10))
    x += 80
  x = -400
  y = -110
  for i in range (10):
    gras(random.randrange(x - 30, x + 30), random.randrange(y + 20, y + 60))
    x += 80
  x = -200
  y = -140
  bob.tracer(5, 0)
  
  bob.width(2)
  
  bob.setheading(0)
  
  bob.up()
  bob.goto(-75, -100)
  bob.down()
  bob.fillcolor(249,249,249)
  
  bob.tracer(100, 0)
  coolshape(side,True)
  bob.tracer(1, 0)
  bob.speed(1)
  bob.speed(side * 5)
  coolshape(side,False)
  
  sideLength = 200 / side * 3.1415
  bob.forward((0.5 * sideLength) - 15)
  bob.left(90)
  bob.forward (40)
  bob.right(90)
  bob.forward(30)
  bob.right(90)
  bob.forward(40)
  bob.up()
  bob.goto(0,-20)
  bob.left(90)
  bob.forward(0.2 * sideLength)
  
  
  
  
  
  
  if side < 30:
    bob.back(side * 0.5)
  else:
    bob.back(30)
  bob.down()
  window()
  bob.up()
  if side == 3:
    bob.back(50)
  elif side > 9:
    bob.back(110)
  elif side == 4:
    bob.back(70)
  else:
    bob.back(100)
  bob.down()
  window()
  
  bob.tracer(5, 0)
  bob.speed(0)
  
  bob.up()
  bob.goto(-75,-100)
  bob.down()
  
  bob.color(100,200,50)
  
  x = -400
  y = -140
  
  bob.tracer(10, 0)
  
  for i in range (10):
    gras(random.randrange(x - 30, x + 30), random.randrange(y - 30, y + 35))
    x += 80
  
  bob.tracer(2, 0)
  
  gras(-65 + 0.2 * sideLength,-105)
  
  flower(-300, -100)
  flower(-170,-150)
  flower(100,-180)
  flower(300, -50)
  bob.penup()
  bob.tracer(5,0)
  print("")
  


#nice!
