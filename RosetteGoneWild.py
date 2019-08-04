# RosetteGoneWild.py
# Billy Ridgeway
# Creates a rosette pattern.

import turtle           # Imports turtle graphics.
t = turtle.Pen()        # Creates a new turtle called t.
t.speed(0)              # Sets the speed of the pen to fast.
turtle.bgcolor("white") # Sets the background color to white.

# Ask the user for the number of circles in the rosette, default to 6.
number_of_circles = int(turtle.numinput("Number of circles",
                                       "How many circles in your rosette?", 6))

for x in range(number_of_circles):      # The range equals how many times it will draw a circle.
    t.circle(100)                       # Sets the size of the circles.
    t.left(360 / number_of_circles)     # How many degrees the circle will shift to the left.
