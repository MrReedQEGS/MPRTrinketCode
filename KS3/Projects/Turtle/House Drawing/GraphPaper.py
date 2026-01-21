import turtle
bob = turtle.Turtle()
bob.speed(0)

def DrawGraphPaper(theTurtle,gridWidth,gridHeight,squareSize):
  theTurtle.color(200,200,200)
  numOfSquaresTall = gridHeight//squareSize
  currentY = -gridHeight//2
  for i in range(numOfSquaresTall):
    theTurtle.penup()
    theTurtle.goto(-gridWidth//2,currentY)
    theTurtle.pendown()
    theTurtle.goto(gridWidth//2,currentY)
    currentY = currentY + squareSize
  
  currentX = -gridWidth//2
  numOfSquaresWide = gridWidth//squareSize
  for i in range(numOfSquaresWide):
    theTurtle.penup()
    theTurtle.goto(currentX,-gridHeight//2)
    theTurtle.pendown()
    theTurtle.goto(currentX,gridHeight//2)
    currentX = currentX + squareSize
  
  theTurtle.penup()
  theTurtle.goto(0,0)
  theTurtle.pendown()
    
DrawGraphPaper(bob,200,400,10)
