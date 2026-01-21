
import turtle
import random,time

WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (82,46,12)
RED = (255,0,0)

# Screen setup
screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("skyblue")
#screen.title("Winter Wonderland with Snowman")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# ---------- Helper Functions ----------

def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# ---------- Background Snow ----------

def draw_snowflakes(count=120):
    t.color("white")
    for _ in range(count):
        t.penup()
        t.goto(random.randint(-840, 640), random.randint(-840, 640))
        t.dot(random.randint(2, 5))



turtle.tracer(0)
t.penup()
t.goto(0,0)
t.pendown()

# ---------- Snowy Ground ----------
draw_rectangle(-450, -200, 900, 200, WHITE)

# ---------- Snowman Body ----------
draw_circle(0, -120, 90, WHITE)   # Bottom
draw_circle(0, 0, 65, WHITE)      # Middle
draw_circle(0, 110, 45, WHITE)    # Head

# ---------- Eyes ----------
draw_circle(-15, 125, 4, "black")
draw_circle(15, 125, 4, "black")

# ---------- Carrot Nose ----------
t.penup()
t.goto(0, 110)
t.pendown()
t.color("orange")
t.begin_fill()
t.goto(40, 105)
t.goto(0, 100)
t.goto(0, 110)
t.end_fill()

# ---------- Mouth ----------
t.penup()
t.goto(-15, 95)
t.pendown()
t.setheading(-60)
t.circle(20, 120)

# ---------- Buttons ----------
draw_circle(0, 20, 5, "black")
draw_circle(0, -10, 5, "black")
draw_circle(0, -40, 5, "black")

# ---------- Hat ----------
draw_rectangle(-20,170,5,90,BROWN)
draw_rectangle(0,160,60,50,BROWN)
draw_rectangle(3,165,15,50,RED)

# ---------- Arms ----------
t.color("brown")
t.width(4)

# Left arm
t.penup()
t.goto(-65, 20)
t.pendown()
t.goto(-130, 60)

# Right arm
t.penup()
t.goto(65, 20)
t.pendown()
t.goto(130, 60)
t.width(1)
turtle.update()
  
while(True):
  turtle.tracer(0)
  draw_snowflakes()
  turtle.update()
  time.sleep(0.1)

# ---------- Finish ----------
turtle.done()
