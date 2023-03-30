# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Use the input() function to prompt the user to enter their weight in kilograms and store the result as a floating point number in the 'weight' variable
weight = float(input("Enter your weight (kg): "))

# Use the input() function to prompt the user to enter their height in meters and store the result as a floating point number in the 'height' variable
height = float(input("Enter your height (m): "))

# Calculate the user's BMI using the weight and height values, rounding the result to three decimal places and storing it in the 'BMI' variable
BMI = round(weight/(height*height), 3)

# Print a message to the console that displays the user's BMI, using an f-string to include the value of the 'BMI' variable in the output string
print(f"Your BMI is: {BMI}")
