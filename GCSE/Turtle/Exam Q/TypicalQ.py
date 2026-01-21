#Similar to a question 3 or 4 - in other words MEDIUM difficulty

#Q9 - Turtle drawing and sub programs
#
# Your program will:
# - import a required library
# - define a sub program that draws a square of any side length filled with any colour
#      def MySquare(someSize,someFillColour)

# - Call the MySquare subprograms 3 times in a row to draw a diagram the meets these requirements:
#     1) 3 squares next to each other.  (Touching)
#     2) The left square will be size 50 and filled red
#     3) The middle square will be size 70 and filled blue
#     4) The right square will be size 20 and filled green
#     5) All outlines will be black in colour

# -------------------------------------------------------------------
# Libraries
# -------------------------------------------------------------------
#=======> Import the required library to draw things on the screen
import turtle

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
#=======> Create one turtle called fred that will be used to do all of your drawing
fred = turtle.Turtle()

# -------------------------------------------------------------------
# Sub programs
# -------------------------------------------------------------------
#=======>finish off the MySquare subprogram that will allow a square of any size to be drawn and filled with any colour.
def MySquare(someSize,someFillColour):
  
    #You may use the globally defined fred turtle in here.
    #theTurtle.pendown()
    fred.begin_fill()
    for side in range(4):
        fred.fillcolor(someFillColour)
        fred.forward(someSize)
        fred.right(90)
    fred.end_fill()
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
#=======> Call the MySquare sub program to draw the left hand square.
sideLength = int(input("How long should the side be?"))
fillColour = input("What colour should fill this in?")
MySquare(sideLength,fillColour)

#=======> Now move the turtle to the bottom left of the middle square.


#=======> Now add the code to draw the other two squares.



#Do not remove this final line of code!
input("Press enter to end the program.")
