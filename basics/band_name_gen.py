# This program is a simple band name generator that prompts the user to enter 
# the name of the city they grew up in and the name of their pet, and then 
# suggests a band name by concatenating these two strings together. The program 
# uses the input() function to get user input, stores the input as strings in 
# the 'city' and 'pet_name' variables, and then prints a message to the console 
# that displays the suggested band name by concatenating the values of these 
# variables together using the string concatenation operator (+).


# Print a message to the console welcoming the user to the band name generator
print("Welcome to band name generator")

# Use the input() function to prompt the user to enter the name of the city they grew up in and store the input as a string in the 'city' variable
city = input("Which city did you grow up in?\n")

# Use the input() function to prompt the user to enter the name of their pet and store the input as a string in the 'pet_name' variable
pet_name = input("What is your pet name?\n")

# Print a message to the console that displays the user's suggested band name, which is the concatenation of the 'city' and 'pet_name' variables
print("Your band name could be: " + city + " " + pet_name)
