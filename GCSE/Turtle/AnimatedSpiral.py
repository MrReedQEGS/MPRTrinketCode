import turtle,time,random

wn = turtle.Screen()
bob = turtle.Turtle()
bob.speed(0)
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
bob.color(r,g,b)

for j in range(20000):
  wn.tracer(0)
  
  if(j%50 ==0):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    bob.color(r,g,b)

  bob.clear()
  
  bob.setheading(j*2)
  bob.penup()
  bob.setpos(0,0)
  bob.pendown()
  for i in range(1000):
    bob.forward(i)
    bob.left(70)
  wn.update() 
  time.sleep(0.01)
