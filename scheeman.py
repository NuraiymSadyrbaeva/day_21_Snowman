# Python code to draw a snowman

import turtle # import turtle module
import time

t = turtle.Turtle() # create a turtle object
t.speed(0) # set the speed to fast
t.pensize(5) # set the pen size to 5
t.color("black") # set the pen color to black

# draw the base circle
t.penup() # lift the pen up
t.goto(0, -200) # move to the position (0, -200)
t.pendown() # put the pen down
t.begin_fill() # start filling the shape
t.circle(100) # draw a circle with radius 100
t.fillcolor("white") # fill the shape with white color
t.end_fill() # end filling the shape

# draw the middle circle
t.penup() # lift the pen up
t.goto(0, -50) # move to the position (0, -50)
t.pendown() # put the pen down
t.begin_fill() # start filling the shape
t.circle(75) # draw a circle with radius 75
t.fillcolor("white") # fill the shape with white color
t.end_fill() # end filling the shape

# draw the head circle
t.penup() # lift the pen up
t.goto(0, 75) # move to the position (0, 75)
t.pendown() # put the pen down
t.begin_fill() # start filling the shape
t.circle(50) # draw a circle with radius 50
t.fillcolor("white") # fill the shape with white color
t.end_fill() # end filling the shape

# draw the eyes
t.penup() # lift the pen up
t.goto(-15, 125) # move to the position (-15, 125)
t.pendown() # put the pen down
t.begin_fill() # start filling the shape
t.circle(5) # draw a circle with radius 5
t.fillcolor("black") # fill the shape with black color
t.end_fill() # end filling the shape
t.penup() # lift the pen up
t.goto(15, 125) # move to the position (15, 125)
t.pendown() # put the pen down
t.begin_fill() # start filling the shape
t.circle(5) # draw a circle with radius 5
t.fillcolor("black") # fill the shape with black color
t.end_fill() # end filling the shape

# draw the nose
t.penup() # lift the pen up
t.goto(0, 115) # move to the position (0, 115)
t.pendown() # put the pen down
t.begin_fill() # start filling the shape
t.right(60) # turn right by 60 degrees
t.forward(25) # move forward by 25 units
t.left(120) # turn left by 120 degrees
t.forward(25) # move forward by 25 units
t.fillcolor("orange") # fill the shape with orange color
t.end_fill() # end filling the shape

# draw the mouth
t.penup() # lift the pen up
t.goto(-25, 100) # move to the position (-25, 100)
t.pendown() # put the pen down
t.right(120) # turn right by 120 degrees
t.circle(25, 180) # draw an arc with radius 25 and angle 180
t.penup() # lift the pen up

#
time.sleep(2)
