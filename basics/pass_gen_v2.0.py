import random

# Define lists of letters, numbers, and symbols to be used in the password.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Prompt the user to enter the length of the password, the number of symbols to include, and the number of numbers to include.
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to hold the password characters.
generated_password = []

# Generate a random letter and add it to the password list `nr_letters` times.
for letter in range(1, nr_letters+1):
    generated_password.append(random.choice(letters))

# Generate a random number and add it to the password list `nr_numbers` times.
for number in range(1, nr_numbers+1):
    generated_password.append(random.choice(numbers))

# Generate a random symbol and add it to the password list `nr_symbols` times.
for symbol in range(1, nr_symbols+1):
    generated_password.append(random.choice(symbols))

# Randomize the order of the password characters.
random.shuffle(generated_password)

# Concatenate the password characters into a string.
delimiter = ""
password = delimiter.join(generated_password)

# Print the generated password as a list and a string, as well as its length.
print(f">> Generated password list is: {generated_password}")
print(f">> Generated password: {password}")
print(f"It's len is : {len(generated_password)}")
