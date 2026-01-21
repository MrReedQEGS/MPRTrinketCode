#free photo editing
#pixlr.com/e

#good 8bit stuff
#https://cutewallpaper.org/24/8-bit-mario-png/view-page-24.html

#png to gif free online
#https://www.zamzar.com/

#if you use a gif they always seem to be upright.  jpg and png rotate to follow the turtle direction.
#This can be helpful sometimes!  :)

import turtle, time

FRAME_RATE = 0.01

floorY = -174
coinTimer = 0
CanJump = True
marioMovingRight = False

def DrawRect(theLength,theWidth,theTurtle):
  for _ in range(2):
    theTurtle.forward(theLength)
    theTurtle.left(90)
    theTurtle.forward(theWidth)
    theTurtle.left(90)

def WriteScore():
  score = turtle.Turtle()
  score.hideturtle()
  score.speed(0)
  score.penup()
  score.goto(60,260)
  score.write("Score : 6423000", font=("Courier", 18, "normal"))
  score.goto(50,250)
  score.pendown()
  score.color("blue")
  DrawRect(240,40,score)
  score.penup()

def WriteCoinText():
  coinText.hideturtle()
  coinText.speed(0)
  coinText.penup()
  coinText.forward(100)
  coinText.goto(-235,260)
  coinText.write(str(numOfCoins) + " coins", font=("Courier", 10, "normal"))

def AddMario(posX,posY):
  
  marioTurtle.hideturtle()
  marioTurtle.shape("finalMarioLeft.png")
  marioTurtle.speed(0)
  marioTurtle.penup()
  marioTurtle.goto(posX,posY)
  marioTurtle.left(90)
  marioTurtle.showturtle()

def AddCoinCollectTotal(posX,posY):
  coinTurtle = turtle.Turtle()
  coinTurtle.hideturtle()
  movingTurtles.append(["coin",coinTurtle])
  coinTurtle.shape(coinFrames[currentCoinFrame])

  coinTurtle.speed(0)
  coinTurtle.left(90)
  coinTurtle.penup()
  coinTurtle.goto(posX,posY)
  coinTurtle.showturtle()

def CoinUpdate(theTurtle):
  global currentCoinFrame
  global coinTimer
  coinTimer = coinTimer + 1
  
  #move the coin to the next animation frame
  if(coinTimer % coinRotationSpeed == 0):
    currentCoinFrame = currentCoinFrame + 1
  
    if(currentCoinFrame > maxCoinFrames):
      #This will put it back to zero next time...
      currentCoinFrame = -1
    else:
      theTurtle.shape(coinFrames[currentCoinFrame])

def AddMush(posX,posY):
  mushTurtle.hideturtle()
  movingTurtles.append(["mush",mushTurtle])
  theScreen.addshape("mush.png")
  mushTurtle.shape("mush.png")

  mushTurtle.speed(0)
  mushTurtle.penup()
  mushTurtle.goto(posX,posY)
  mushTurtle.left(90)
  mushTurtle.showturtle()

def MushMove(theTurtle):
  global mushX
  global mushDirection
  if(mushX > mushMaxX or mushX < mushMinX):
    mushDirection = -mushDirection
    
  mushX = mushX + (2 * mushDirection)
  theTurtle.goto(mushX,mushY)

def AddCoins():
  #put some coins on the screen for mario to collect
  currentX = -270
  for i in range(5):
    someCoinTurtle = turtle.Turtle()
    someCoinTurtle.hideturtle()
    someCoinTurtle.speed(0)
    someCoinTurtle.penup()
    someCoinTurtle.goto(currentX,-160)
    someCoinTurtle.shape("coinFrame1.png")
    currentX = currentX + 50
    collisionList.append(["coin",someCoinTurtle])
    someCoinTurtle.showturtle()
  
  someCoinTurtle = turtle.Turtle()
  someCoinTurtle.hideturtle()
  someCoinTurtle.speed(0)
  someCoinTurtle.penup()
  someCoinTurtle.goto(260,-100)
  someCoinTurtle.shape("coinFrame1.png")
  collisionList.append(["coin",someCoinTurtle])
  someCoinTurtle.showturtle()
  
  

###########################################################

def Up():
  #Good jump code from Ben in year 10!
  global CanJump
  y = 0
  ystep = 12
  ystepAll = 12
  if(CanJump == True):
    CanJump = False
    while(ystep >= -1 * ystepAll):
      time.sleep(FRAME_RATE)
      myX = marioTurtle.xcor()
      myY = marioTurtle.ycor()
      myY = myY + ystep
      marioTurtle.goto(myX,myY)
      ystep = ystep - 1
      
    #put him on the floor if needed
    if(marioTurtle.ycor() != floorY):
      marioTurtle.goto(marioTurtle.xcor(),floorY)
    CanJump = True

def Left():
  global marioMovingRight
  marioMovingRight = False
  myX = marioTurtle.xcor()
  myY = marioTurtle.ycor()
  myX = myX - 5
  marioTurtle.goto(myX,myY)
  if(marioIsBig):
    marioTurtle.shape("finalMarioLeftBig.png")
  else:
    marioTurtle.shape("finalMarioLeft.png")

def Right():
  global marioMovingRight
  marioMovingRight = True
  myX = marioTurtle.xcor()
  myY = marioTurtle.ycor()
  myX = myX + 5
  marioTurtle.goto(myX,myY)
  if(marioIsBig):
    marioTurtle.shape("finalMarioBig.png")
  else:
    marioTurtle.shape("finalMario.jpg")

###########################################################

def UpdateCoinsText():
  coinText.hideturtle()
  coinText.clear()
  coinText.hideturtle()
  WriteCoinText()

def CoinSound():
  #playsound('audio.mp3')
  pass

#MAIN BODY
theScreen = turtle.Screen()
theScreen.setup(width=600,height=600)
theScreen.bgpic("mario back 1.png")
#theScreen.bgcolor(0,255,0)
theScreen.addshape("finalMario.jpg")
theScreen.addshape("finalMarioLeft.png")
theScreen.addshape("finalMarioBig.png")
theScreen.addshape("finalMarioLeftBig.png")
marioIsBig = False

coinText = turtle.Turtle()
coinText.hideturtle()
mushTurtle = turtle.Turtle()
mushTurtle.hideturtle()

movingTurtles = []
collisionList = []
collisionList.append(["mush",mushTurtle])

currentCoinFrame = 0
maxCoinFrames = 3
coinRotationSpeed = 5
coinFrames = ["coinFrame1.png","coinFrame1b.png","coinFrame2.png","coinFrame3.png"]
for i in range(0,maxCoinFrames+1):
    theScreen.addshape(coinFrames[i])

AddCoins()

marioTurtle = turtle.Turtle()
marioTurtle.hideturtle()
AddMario(-20,-170)

numOfCoins = 0
mushX = 70
mushY = floorY
mushMinX = mushX
mushMaxX = 215
mushDirection = 1
AddMush(mushX,mushY)
AddCoinCollectTotal(-265,265)
WriteCoinText()
WriteScore()

#keyboard handling
theScreen.onkey(Up, "Up")
theScreen.onkey(Right, "Right")
theScreen.onkey(Left, "Left")
theScreen.listen()

while(True):
  
  time.sleep(FRAME_RATE)
  
  for someTurtle in movingTurtles:
    turtleName = someTurtle[0]
    theTurtle = someTurtle[1]

    if(turtleName == "coin"):
      CoinUpdate(theTurtle)
    elif(turtleName == "mush"):
      MushMove(theTurtle)
      
  #look for collisions?
  
  for someTurtle in collisionList:
    typeOfThing = someTurtle[0]
    theTurtle = someTurtle[1]
    currentMarioX = marioTurtle.xcor()
    if(currentMarioX-30 < theTurtle.xcor() and currentMarioX > theTurtle.xcor() - 30):
      theTurtle.hideturtle()
      collisionList.remove(someTurtle)
        
      if(typeOfThing == "coin"):
        numOfCoins = numOfCoins + 1
        UpdateCoinsText()
        CoinSound()
      elif(typeOfThing == "mush"):
        floorY = -154
        marioIsBig = True
        myX = marioTurtle.xcor()
        myY = marioTurtle.ycor()
        
        if(marioMovingRight):
          marioTurtle.shape("finalMarioBig.png")
        else:
          marioTurtle.shape("finalMarioLeftBig.png")
  
  if(marioTurtle.ycor() < floorY):
      marioTurtle.goto(marioTurtle.xcor(),floorY)
  
  
