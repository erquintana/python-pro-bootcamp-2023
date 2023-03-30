# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# Use the input() function to prompt the user to enter their weight in kilograms and store the result as a floating point number in the 'weight' variable
weight = float(input("Enter your weight (kg): "))

# Use the input() function to prompt the user to enter their height in meters and store the result as a floating point number in the 'height' variable
height = float(input("Enter your height (m): "))

# Calculate the user's BMI using the weight and height values, rounding the result to three decimal places and storing it in the 'BMI' variable
BMI = round(weight/(height*height), 3)

# Check the value of BMI to determine the BMI state
if (BMI < 18.5):
    BMI_state = "underweight"
elif (BMI > 18.5 and BMI <= 25):
    BMI_state = "normal weight"
elif (BMI > 25 and BMI <= 30):
    BMI_state = "slightly overweight"
elif (BMI > 30 and BMI <= 35):
    BMI_state = "obese"
elif (BMI > 35):
    BMI_state = "clinically obese"

# Print a message to the console that displays the user's BMI, using an f-string to include the value of the 'BMI' variable in the output string
print(f"Your BMI is: {BMI} and you are {BMI_state}")
