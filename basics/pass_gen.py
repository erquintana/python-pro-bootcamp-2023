# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_password = ""
total_chars = nr_letters + nr_symbols + nr_numbers
new_char = ""

print("\n")
while(len(generated_password) < total_chars):
    
    rdm_char = random.randint(0, 2)
    print("rdn = ", rdm_char)
    
    if(rdm_char == 0 and nr_letters > 0 ):
        rdm_l = random.randint(0, len(letters)-1)
        new_char = letters[rdm_l]
        nr_letters -= 1
        generated_password += str(new_char)
    elif(rdm_char == 1 and nr_numbers > 0):
        rdm_n = random.randint(0, len(numbers)-1)
        new_char = numbers[rdm_n]
        nr_numbers -= 1
        generated_password += str(new_char)
    elif(rdm_char == 2 and nr_symbols > 0):
        rdm_s = random.randint(0, len(symbols)-1)
        new_char = symbols[rdm_s]
        nr_symbols -= 1
        generated_password += str(new_char)

    print(f"{len(generated_password)} : {str(new_char)}")

print(f">> Generated password is: {generated_password}")
print(f"It's len is : {len(generated_password)}")