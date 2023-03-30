# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Prompt the user to enter a two-digit number and store the input as a string in the variable 'two_digit_number'
two_digit_number = input("Please, enter a 2 digit number\n")

# Extract the first digit of the two-digit number by accessing the character at index 0 of the 'two_digit_number' string, convert it to an integer, and store it in the variable 'digit_1'
digit_1 = int(two_digit_number[0])

# Extract the second digit of the two-digit number by accessing the character at index 1 of the 'two_digit_number' string, convert it to an integer, and store it in the variable 'digit_2'
digit_2 = int(two_digit_number[1])

# Add the values of 'digit_1' and 'digit_2' and store the result in the variable 'sum'
sum = digit_1 + digit_2

# Print a message to the console that displays the equation and the result of the sum using the values of 'digit_1', 'digit_2', and 'sum'
print("sum = ",digit_1," + ", digit_2, " = ", sum)
