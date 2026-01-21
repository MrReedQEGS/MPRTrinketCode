import turtle

bKeepLooping = True

BOX_HEIGHT = 25
GRID_SIZE = 18

jeff = turtle.Turtle()

def drawGrid():
  jeff.color("#aeb8b1")
  jeff.speed(0)
  jeff.right(90)
  jeff.penup()
  jeff.forward(BOX_HEIGHT*(GRID_SIZE//2))
  jeff.right(90)
  jeff.forward(BOX_HEIGHT*12-BOX_HEIGHT//2)
  jeff.right(90)
  jeff.pendown()
  jeff.forward(BOX_HEIGHT*GRID_SIZE)
  
  for i in range(GRID_SIZE//2):
    jeff.right(90)
    jeff.forward(BOX_HEIGHT)
    jeff.right(90)
    jeff.forward(BOX_HEIGHT*GRID_SIZE)
    jeff.left(90)
    jeff.forward(BOX_HEIGHT)
    jeff.left(90)
    jeff.forward(BOX_HEIGHT*GRID_SIZE)
    
  jeff.left(90)
  jeff.forward(BOX_HEIGHT*GRID_SIZE)
  jeff.right(-90)
  jeff.forward(BOX_HEIGHT)
  jeff.left(90)
  jeff.forward(BOX_HEIGHT*GRID_SIZE)
  jeff.right(90)
  jeff.forward(BOX_HEIGHT)
  jeff.right(90)
  
  for i in range(GRID_SIZE//2 - 1):
    jeff.forward(BOX_HEIGHT*GRID_SIZE)
    jeff.left(90)
    jeff.forward(BOX_HEIGHT)
    jeff.left(90)
    jeff.forward(BOX_HEIGHT*GRID_SIZE)
    jeff.right(90)
    jeff.forward(BOX_HEIGHT)
    jeff.right(90)
  
  jeff.forward(BOX_HEIGHT*GRID_SIZE)

def click(clickX, clickY):
  clickY  = clickY + BOX_HEIGHT//2
  
  #The mouse y click location was not quite working and the above "hack"
  #fixes it so the correct box is coloured in.  Don't worry about it....it works!
  
  global ofclickX
  global ofclickY
  global clicked
  
  #Try to find nearest grid corner
  if(clickX%20 != 0):
    #it is not on the grid in the x direction so
    #round it to the nearest 20 then move it 10...it works!!!  :)
    ofclickX = int(round(clickX/BOX_HEIGHT)*BOX_HEIGHT) + BOX_HEIGHT//2
  else:
    ofclickX = clickX + BOX_HEIGHT//2
  
  #Try to find nearest grid corner
  if(clickY%20 != 0):
    ofclickY = int(round(clickY/BOX_HEIGHT)*BOX_HEIGHT)
  else:
    ofclickY = clickY
    
  #Draw the square in the correct location and colour it in.
  jeff.speed(0)
  jeff.penup()
  jeff.goto(ofclickX,ofclickY)
  jeff.pendown()
  jeff.begin_fill()
  for i in range(4):
    jeff.forward(BOX_HEIGHT)
    jeff.left(90)
  jeff.end_fill()
  
theScreen = turtle.Screen()
theScreen.setup(width=BOX_HEIGHT*GRID_SIZE*2,height=BOX_HEIGHT*GRID_SIZE*2)
#theScreen.bgpic("wp7664490.jpeg")

# CLICK DETECTION
jeff.hideturtle()
drawGrid()
jeff.fillcolor("Blue")
while(bKeepLooping == True):
  theScreen.onclick(click)

  
