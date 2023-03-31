# This program creates a turtle that can move and draw on the screen.

from turtle import Turtle, Screen  # Import the Turtle and Screen classes from the turtle module

# Create a turtle object and a screen object
tim = Turtle()
screen = Screen()

# Define functions for moving and turning the turtle, and clearing the screen
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Set up event listeners for specific keys on the keyboard
screen.listen()  # Listen for keyboard input
screen.onkey(move_forwards, "Up")  # When "Up" arrow is pressed, call the move_forwards function
screen.onkey(move_backwards, "Down")  # When "Down" arrow is pressed, call the move_backwards function
screen.onkey(turn_left, "Left")  # When "Left" arrow is pressed, call the turn_left function
screen.onkey(turn_right, "Right")  # When "Right" arrow is pressed, call the turn_right function
screen.onkey(clear, "c")  # When "c" is pressed, call the clear function

# Keep the screen open until the user clicks to close it
screen.exitonclick()
