# -*- coding: utf-8 -*-
"""CSC101Lesson1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/zugurbil/CSC101/blob/main/CSC101Lesson1.ipynb

Question 1
"""

def display_info():
    title = "To Kill a Mockingbird"
    author = "Harper Lee"
    description = "A novel set in the 1930s South, tackling issues of racism and justice through the eyes of a young girl named Scout Finch."

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Description: {description}")

display_info()

"""Question 2"""

def london_attractions():
    print("Top attractions in London:")
    print("- The British Museum")
    print("- Tower of London")
    print("- Buckingham Palace")
    print("- London Eye")

def paris_attractions():
    print("Top attractions in Paris:")
    print("- Eiffel Tower")
    print("- Louvre Museum")
    print("- Notre-Dame Cathedral")
    print("- Montmartre")

def new_york_attractions():
    print("Top attractions in New York:")
    print("- Statue of Liberty")
    print("- Central Park")
    print("- Metropolitan Museum of Art")
    print("- Times Square")

# Call the functions
london_attractions()
paris_attractions()
new_york_attractions()

"""Question 3"""

!pip3 install ColabTurtle

initializeTurtle()

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

"""Question 4"""

def find_even_numbers():
    even_numbers = []
    for number in range(0, 11):
        if number % 2 == 0:
            even_numbers.append(number)
    print("Even numbers between 0 and 10:", even_numbers)

find_even_numbers()