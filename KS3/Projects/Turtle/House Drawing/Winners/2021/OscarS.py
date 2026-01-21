import turtle
z = turtle.Turtle()
z.speed(0)
drawingArea = turtle.Screen()
drawingArea.bgcolor(180, 201, 212)

#draw the base

#blue line
z.width(8)
z.color(23, 70, 94)
z.penup()
z.goto(-150,-100)
z.pendown()
z.forward(340)
#red line
z.width(1)
z.penup()
z.color("red")
z.goto(-150,-100)
z.forward(70)
z.left(90)
z.forward(5)
z.right(90)
z.pendown()
z.forward(200)
#bottem part of the house
#(box kinda bit)
z.begin_fill()
z.color("white")
z.left(90)
z.forward(100)
z.left(90)
z.forward(200)
z.left(90)
z.forward(100)
z.end_fill()
#roof outline
z.penup()
z.color(23, 70, 94)
z.left(180)
z.forward(100)
z.left(90)
z.pendown()

z.begin_fill()
z.forward(20)
z.right(90)
z.right(30)
z.forward(66)

z.left(180)
z.forward(66)
z.left(120)
z.forward(20)
z.forward(200)

z.forward(20)
z.left(90)
z.left(30)
z.forward(65)
z.left(60)
z.forward(175)


z.left(60)
z.forward(65)
z.left(90)
z.left(30)
z.forward(20)
z.end_fill()

#line in the middle of the house :)

z.penup()
z.right(90)
z.forward(50)
z.left(90)
z.pendown()
z.forward(75)
z.penup()
z.forward(50)
z.pendown()
z.forward(75)

#attempt at windows

z.penup()
z.back(200)
z.forward(10)
z.left(90)
z.forward(10)


#window frame

z.color("grey")
z.pendown()
z.width(2)

z.begin_fill()
z.forward(30)
z.right(90)
z.forward(25)
z.right(90)
z.forward(30)
z.right(90)
z.forward(25)
z.fillcolor(23, 70, 94)
z.end_fill()

#individual panes of glass

z.penup()
z.right(90)
z.forward(15)
z.right(90)
z.color("white")
z.pendown()
z.forward(25)
z.penup()
z.left(90)
z.forward(15)
z.left(90)
z.forward(12.5)
z.left(90)
z.pendown()
z.forward(30)


# repositioning for second

z.penup()
z.color("black")
z.left(90)
z.forward(12.5)
z.forward(10)
z.left(90)

#second window

z.color("grey")
z.pendown()
z.width(2)

z.begin_fill()
z.forward(30)
z.right(90)
z.forward(25)
z.right(90)
z.forward(30)
z.right(90)
z.forward(25)
z.fillcolor(23, 70, 94)
z.end_fill()

#individual panes of glass

z.penup()
z.right(90)
z.forward(15)
z.right(90)
z.color("white")
z.pendown()
z.forward(25)
z.penup()
z.left(90)
z.forward(15)
z.left(90)
z.forward(12.5)
z.left(90)
z.pendown()
z.forward(30)

#third window

#repositioning

z.penup()
z.right(90)
z.forward(60)
z.left(90)
z.forward(60)
z.left(90)
z.forward(12.5)
z.left(90)
z.forward(10)
z.color("black")

#third window

z.color("grey")
z.pendown()
z.width(2)

z.begin_fill()
z.forward(30)
z.right(90)
z.forward(25)
z.right(90)
z.forward(30)
z.right(90)
z.forward(25)
z.fillcolor(23, 70, 94)
z.end_fill()

#individual panes of glass

z.penup()
z.right(90)
z.forward(15)
z.right(90)
z.color("white")
z.pendown()
z.forward(25)
z.penup()
z.left(90)
z.forward(15)
z.left(90)
z.forward(12.5)
z.left(90)
z.pendown()
z.forward(30)

#fourth window

z.penup()
z.color("black")
z.left(90)
z.forward(12.5)
z.forward(10)
z.left(90)

#repositioning

z.color("grey")
z.pendown()
z.width(2)

z.begin_fill()
z.forward(30)
z.right(90)
z.forward(25)
z.right(90)
z.forward(30)
z.right(90)
z.forward(25)
z.fillcolor(23, 70, 94)
z.end_fill()

#individual panes of glass

z.penup()
z.right(90)
z.forward(15)
z.right(90)
z.color("white")
z.pendown()
z.forward(25)
z.penup()
z.left(90)
z.forward(15)
z.left(90)
z.forward(12.5)
z.left(90)
z.pendown()
z.forward(30)

# right side of windows

z.penup()
z.forward(10)
z.left(90)
z.color("black")
z.forward(70)

z.left(90)
z.forward(10)





z.color("grey")
z.pendown()
z.width(2)

z.begin_fill()
z.forward(30)
z.right(90)
z.forward(25)
z.right(90)
z.forward(30)
z.right(90)
z.forward(25)
z.fillcolor(23, 70, 94)
z.end_fill()

#individual panes of glass

z.penup()
z.right(90)
z.forward(15)
z.right(90)
z.color("white")
z.pendown()
z.forward(25)
z.penup()
z.left(90)
z.forward(15)
z.left(90)
z.forward(12.5)
z.left(90)
z.pendown()
z.forward(30)

#fourth window

z.penup()
z.color("black")
z.left(90)
z.forward(12.5)
z.forward(10)
z.left(90)

#repositioning

z.color("grey")
z.pendown()
z.width(2)

z.begin_fill()
z.forward(30)
z.right(90)
z.forward(25)
z.right(90)
z.forward(30)
z.right(90)
z.forward(25)
z.fillcolor(23, 70, 94)
z.end_fill()

#individual panes of glass

z.penup()
z.right(90)
z.forward(15)
z.right(90)
z.color("white")
z.pendown()
z.forward(25)
z.penup()
z.left(90)
z.forward(15)
z.left(90)
z.forward(12.5)
z.left(90)
z.pendown()
z.forward(30)

#fouth set of windows

z.penup()
z.color("black")
z.back(40)
z.right(90)
z.forward(47)
z.right(90)
z.forward(10)

#repositioning

z.color("grey")
z.pendown()
z.width(2)

z.begin_fill()
z.forward(30)
z.right(90)
z.forward(25)
z.right(90)
z.forward(30)
z.right(90)
z.forward(25)
z.fillcolor(23, 70, 94)
z.end_fill()

#individual panes of glass

z.penup()
z.right(90)
z.forward(15)
z.right(90)
z.color("white")
z.pendown()
z.forward(25)
z.penup()
z.left(90)
z.forward(15)
z.left(90)
z.forward(12.5)
z.left(90)
z.pendown()
z.forward(30)

# right side of windows

z.penup()
z.forward(10)
z.left(90)
z.color("black")
z.forward(22.5)

z.left(90)
z.forward(10)





z.color("grey")
z.pendown()
z.width(2)

z.begin_fill()
z.forward(30)
z.right(90)
z.forward(25)
z.right(90)
z.forward(30)
z.right(90)
z.forward(25)
z.fillcolor(23, 70, 94)
z.end_fill()

#individual panes of glass

z.penup()
z.right(90)
z.forward(15)
z.right(90)
z.color("white")
z.pendown()
z.forward(25)
z.penup()
z.left(90)
z.forward(15)
z.left(90)
z.forward(12.5)
z.left(90)
z.pendown()
z.forward(30)

#door!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#repositioning

z.penup()
z.color("black")
z.goto(-150,-100)
z.left(90)
z.forward(150)  #amount in on blue line

# two blue lines

z.left(90)
z.forward(5)
z.forward(3)
z.right(90)
z.color(47, 97, 156)
z.width(4)
z.pendown()
z.forward(40)

z.penup()
z.left(90)
z.forward(5)
z.left(90)
z.forward(5)
z.pendown()
z.width(3)
z.forward(30)

#door frame

z.width(1)
z.penup()
z.forward(5)
z.left(90)
z.forward(3)
z.color("grey")
z.left(180)
z.pendown()
z.forward(60)
z.right(90)
z.forward(40)
z.right(90)
z.forward(60)
z.back(60)
z.right(90)
z.back(3)
z.width(3)
z.color(23, 70, 94)
z.forward(46)


#detail within the door

#main block in door

z.penup()
z.back(3)
z.left(90)
z.forward(50)
z.left(90)
z.forward(8)
z.pendown()
z.width(1)
z.begin_fill()
z.forward(24)
z.left(90)
z.forward(35)
z.left(90)
z.forward(24)
z.left(90)
z.forward(35)
z.end_fill()
z.left(90)
z.forward(12)
z.color("white")
z.left(90)
z.width(3)
z.forward(35)
z.width(1)

z.penup()
z.left(90)
z.forward(13)
z.right(90)
z.forward(5)
z.color(23, 70, 94)


#little boxs at top

z.begin_fill()
z.forward(7)
z.right(90)
z.forward(3)
z.right(90)
z.forward(7)
z.right(90)
z.forward(3)
z.end_fill()

#repositioning

z.right(180)
z.forward(6)
z.left(90)

#more!!!!!!!!!!!!!!!!

z.begin_fill()
z.forward(7)
z.right(90)
z.forward(3)
z.right(90)
z.forward(7)
z.right(90)
z.forward(3)
z.end_fill()
z.right(180)
z.forward(6)
z.left(90)

z.begin_fill()
z.forward(7)
z.right(90)
z.forward(3)
z.right(90)
z.forward(7)
z.right(90)
z.forward(3)
z.end_fill()
z.right(180)
z.forward(6)
z.left(90)

z.begin_fill()
z.forward(7)
z.right(90)
z.forward(3)
z.right(90)
z.forward(7)
z.right(90)
z.forward(3)
z.end_fill()
z.right(180)
z.forward(6)
z.left(90)

z.begin_fill()
z.forward(7)
z.right(90)
z.forward(3)
z.right(90)
z.forward(7)
z.right(90)
z.forward(3)
z.end_fill()
z.right(180)
z.forward(6)
z.left(90)

#chimney

# repositioning

z.penup()
z.goto(75,75)
z.left(180)
z.forward(15)
z.right(90)
z.forward(40)
z.color(237, 81, 81)

#red bit

z.begin_fill()
z.pendown()
z.right(90)
z.forward(13)
z.left(90)
z.forward(25)
z.left(90)
z.forward(28)
z.left(90)
z.forward(25)
z.left(90)
z.forward(28)
z.end_fill()

#white colours with red stripe

z.begin_fill()
z.color("white")
z.forward(5)
z.left(90)
z.forward(25)
z.left(90)
z.forward(5)
z.left(90)
z.forward(25)
z.end_fill()

#red bit / stripe

z.left(90)
z.forward(5)

z.begin_fill()
z.color(237, 81, 81)
z.forward(3)
z.left(90)
z.forward(25)
z.left(90)
z.forward(3)
z.left(90)
z.forward(25)
z.left(90)
z.forward(3)
z.right(90)

z.end_fill()

# top white bit

z.begin_fill()
z.color("white")
z.forward(3)
z.left(90)
z.forward(6)
z.left(90)
z.forward(31)
z.left(90)
z.forward(6)
z.left(90)
z.forward(31)
z.end_fill()

#white lines on the roof :)

#line 1
z.penup()
z.forward(10)
z.right(90)
z.forward(30)
z.left(90)
z.pendown()
z.forward(35)

z.penup()
z.left(180)
z.forward(90)
z.pendown()
z.forward(25)

z.penup()
z.forward(42)
z.pendown()
z.back(10)


#line two

z.penup()
z.left(90)
z.forward(10)
z.left(90)
z.forward(160)
z.pendown()
z.forward(25)

#line three

z.penup()
z.right(90)
z.forward(3)
z.right(90)
z.forward(123)
z.pendown()
z.forward(80)

#line four

z.penup()
z.left(90)
z.forward(4)
z.left(90)
z.forward(100)
z.pendown()
z.forward(90)

#line five

z.penup()
z.right(90)
z.forward(3)
z.right(90)
z.forward(115)
z.pendown()
z.forward(30)

#line five

z.penup()
z.left(90)
z.forward(10)
z.right(90)
z.forward(51)
z.pendown()
z.back(95)
z.penup()
z.back(15)
z.pendown()
z.back(30)
z.penup()
z.back(30)
z.pendown()
z.back(30)

#line six (mini line)

z.penup()
z.left(90)
z.forward(5)
z.right(90)
z.forward(35)
z.pendown()
z.forward(20)

# testing chimney cloud

z.penup()
z.right(90)
z.forward(85)
z.left(90)
z.forward(27)
z.right(90)

#actual cloud

z.color("grey")
z.begin_fill()
z.circle(10,360)
z.end_fill()

#some more?

z.forward(10)
z.left(90)
z.forward(15)
z.right(90)

z.color("grey")
z.begin_fill()
z.circle(10,360)
z.end_fill()

z.forward(10)
z.left(90)
z.forward(15)
z.right(90)

z.color("grey")
z.begin_fill()
z.circle(10,360)
z.end_fill()

# starting on the outside :)

#repositioning
z.penup()
z.left(180)
z.forward(216)
z.right(90)
z.forward(80)
z.forward(30)
z.right(90)

#lampost

z.pendown()
z.color("black")
z.width(3)
z.forward(20)
z.width(1)
z.forward(40)
z.right(90)

z.begin_fill()
z.forward(5)
z.back(10)
z.left(90)
z.left(7)
z.width(1)
z.forward(20)
z.back(20)
z.right(100)
z.forward(10)
z.left(87)
z.forward(20)
z.right(84)
z.forward(3)
z.width(4)
z.back(21.5)
z.forward(21.5)
z.width(1)
z.fillcolor(191, 214, 227)
z.end_fill()

z.forward(-10.25)
z.fillcolor("black")
z.left(90)
z.width(4)
z.forward(3)

#flame

z.penup()
z.width(1)
z.left(180)
z.forward(20.9)
z.left(90)
z.forward(3.5)
z.left(90)
z.color("orange")
z.begin_fill()
z.circle(3,180)
z.end_fill()


#second lampost :)

z.penup()
z.forward(63.5)
z.left(90)
z.forward(234)
z.forward(30)
z.left(90)

#lampost

z.pendown()
z.color("black")
z.width(3)
z.forward(20)
z.width(1)
z.forward(40)
z.right(90)

z.begin_fill()
z.forward(5)
z.back(10)
z.left(90)
z.left(7)
z.width(1)
z.forward(20)
z.back(20)
z.right(100)
z.forward(10)
z.left(87)
z.forward(20)
z.right(84)
z.forward(3)
z.width(4)
z.back(21.5)
z.forward(21.5)
z.width(1)
z.fillcolor(191, 214, 227)
z.end_fill()

z.forward(-10.25)
z.fillcolor("black")
z.left(90)
z.width(4)
z.forward(3)

#flame

z.penup()
z.width(1)
z.left(180)
z.forward(20.9)
z.left(90)
z.forward(3.5)
z.left(90)
z.color("orange")
z.begin_fill()
z.circle(3,180)
z.end_fill()

#little pricket fence

#repos

z.forward(60)
z.right(90)
z.forward(27)
z.left(180)
z.forward(5)
z.left(90)

#start of the fence

z.pendown()
z.color("white")
z.begin_fill()
z.forward(30)
z.right(90)
z.forward(7)
z.right(90)
z.forward(30)
z.right(90)
z.forward(7)
z.back(7)
z.end_fill()
z.penup()
z.back(8)
z.right(90)

#couple more

z.pendown()
z.color("white")
z.begin_fill()
z.forward(30)
z.right(90)
z.forward(7)
z.right(90)
z.forward(30)
z.right(90)
z.forward(7)
z.back(7)
z.end_fill()
z.penup()
z.back(8)
z.right(90)



z.pendown()
z.color("white")
z.begin_fill()
z.forward(30)
z.right(90)
z.forward(7)
z.right(90)
z.forward(30)
z.right(90)
z.forward(7)
z.back(7)
z.end_fill()
z.penup()
z.back(8)
z.right(90)

z.pendown()
z.color("white")
z.begin_fill()
z.forward(30)
z.right(90)
z.forward(7)
z.right(90)
z.forward(30)
z.right(90)
z.forward(7)
z.back(7)
z.end_fill()

#now the wooden latch across the pricket fence

z.right(90)
z.forward(11.5)
z.left(90)
z.begin_fill()
z.forward(53)
z.right(90)
z.forward(7)
z.right(90)
z.forward(53)
z.right(90)
z.forward(7)
z.end_fill()



# fence on the left hand side

#repos

z.penup()
z.forward(11.5)
z.right(90)
z.forward(317)
z.right(90)


# pricket fence

z.pendown()
z.color("white")
z.begin_fill()
z.forward(30)
z.right(90)
z.forward(7)
z.right(90)
z.forward(30)
z.right(90)
z.forward(7)
z.back(7)
z.end_fill()
z.penup()
z.back(8)
z.right(90)

#couple more

z.pendown()
z.color("white")
z.begin_fill()
z.forward(30)
z.right(90)
z.forward(7)
z.right(90)
z.forward(30)
z.right(90)
z.forward(7)
z.back(7)
z.end_fill()
z.penup()
z.back(8)
z.right(90)



z.pendown()
z.color("white")
z.begin_fill()
z.forward(30)
z.right(90)
z.forward(7)
z.right(90)
z.forward(30)
z.right(90)
z.forward(7)
z.back(7)
z.end_fill()
z.penup()
z.back(8)
z.right(90)

z.pendown()
z.color("white")
z.begin_fill()
z.forward(30)
z.right(90)
z.forward(7)
z.right(90)
z.forward(30)
z.right(90)
z.forward(7)
z.back(7)
z.end_fill()

#now the wooden latch across the pricket fence

z.right(90)
z.forward(11.5)
z.left(90)
z.begin_fill()
z.forward(53)
z.right(90)
z.forward(7)
z.right(90)
z.forward(53)
z.right(90)
z.forward(7)
z.end_fill()




z.color("black")
z.penup()

z.forward(75)
z.left(90)
z.forward(30)
z.write("A little village house, by oscar smith")


z.forward(500)
