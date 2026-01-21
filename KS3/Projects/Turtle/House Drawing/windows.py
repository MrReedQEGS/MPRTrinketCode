#This code could be used to draw windows or bricks using a LOOP
import turtle,random
bob = turtle.Turtle()
bob.speed(9)

###########################################
#SUBPROGRAMS
###########################################

#Tell the computer what a window looks like
def DrawWindow():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color = (r,g,b)
  bob.fillcolor(color)
  bob.begin_fill()
  for i in range(2):
    bob.forward(10)
    bob.left(90)
    bob.forward(20)
    bob.left(90)
  bob.end_fill()

###########################################
#MAIN PROGRAM
###########################################

#move to start location for first window
bob.penup()
bob.goto(-100,0)
bob.pendown()

#Now draw 15 windows    
for i in range(3):
  
  DrawWindow()
  #Move to new location before we draw the next one!
  bob.penup()
  bob.forward(15)
  bob.pendown()
  



