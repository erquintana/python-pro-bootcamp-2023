from turtle import Turtle, Screen
import random

# Flag to keep track if race is ongoing
is_race_on = False

# Create a screen with specific dimensions
screen = Screen()
screen.setup(width=500, height=400)

# Ask user to make a bet and get the color of the turtle they bet on
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define a list of colors and Y positions for each turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Create a list to store all the turtle objects
all_turtles = []

# Create 6 turtles, set their attributes, and add them to the all_turtles list
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# If user made a bet, set is_race_on to True to start the race
if user_bet:
    is_race_on = True

# While the race is ongoing, move each turtle a random amount until a turtle wins the race
while is_race_on:
    for turtle in all_turtles:
        # Check if the turtle has reached the right end of the screen
        if turtle.xcor() > 230:
            # End the race and get the winning turtle's color
            is_race_on = False
            winning_color = turtle.pencolor()
            # Check if the user's bet is correct and print the outcome
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        # Move the turtle a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Close the screen when the user clicks on it
screen.exitonclick()
