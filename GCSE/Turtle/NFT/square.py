import turtle, random
bob = turtle.Turtle()
bob.speed(0)
bob.hideturtle()
sideLen = 3
turtle.tracer(0,0)
numOfPixels = 64
bottLeftX = -180
bottLeftY = -190
gap = 2

def DrawARectangle(x,y,someWidth,someLength,someCol):
  bob.penup()
  bob.setpos(x,y)
  bob.pendown()
  bob.fillcolor(someCol)
  bob.begin_fill()
  for i in range(2):
    bob.forward(someLength)
    bob.left(90)
    bob.forward(someWidth)
    bob.left(90)
  bob.end_fill()

#Main program
#Draw main rect - medium grey

DrawARectangle(bottLeftX-gap,bottLeftY-gap,(sideLen+gap)*numOfPixels+gap,(sideLen+gap)*numOfPixels+gap,"grey")

for j in range(numOfPixels):
  for i in range(numOfPixels):
    someRed=random.randint(0,255)
    someGreen=random.randint(0,255)
    someBlue=random.randint(0,255)
    
    #someRed=0
    #someGreen=0
    #someBlue=0
    
    DrawARectangle(bottLeftX + i*(sideLen+gap) ,bottLeftY + j*(sideLen+gap),sideLen,sideLen,(someRed,someGreen,someBlue))

turtle.update()
