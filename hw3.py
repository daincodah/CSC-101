# -*- coding: utf-8 -*-
"""CSC101Lesson1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/zugurbil/CSC101/blob/main/CSC101Lesson1.ipynb
"""

!pip3 install ColabTurtle
from ColabTurtle.Turtle import *

initializeTurtle()

"""Question 1"""

# Import ColabTurtle for Google Colab
import ColabTurtle.Turtle as turtle

# Initialize Turtle window
turtle.initializeTurtle()  # No arguments needed

# 1. Draw an 8-sided octagon
turtle.color("blue")
turtle.pendown()
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.penup()
turtle.home()

"""Question 2"""

# Import ColabTurtle for Google Colab
import ColabTurtle.Turtle as turtle

# Initialize Turtle window
turtle.initializeTurtle()  # No arguments needed

turtle.color("red")
turtle.pendown()
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.penup()

# Move to a new position for the second star
turtle.goto(150, 50)
turtle.pendown()

# Draw the second five-pointed star in green
turtle.color("green")
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.penup()
turtle.home()

"""Question 3"""

# Import ColabTurtle for Google Colab
import ColabTurtle.Turtle as turtle

# Initialize Turtle window
turtle.initializeTurtle()  # No arguments needed

turtle.color("purple")
for i in range(36):
    turtle.pendown()
    turtle.forward(i * 5)
    turtle.right(144)
turtle.penup()
turtle.home()

"""Question 4"""

for i in range(1, 4):  # Adjust the range for more rows
    print("*" * i)