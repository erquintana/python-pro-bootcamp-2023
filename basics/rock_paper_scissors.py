import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# import the random module to generate random numbers
import random

# define a list of images for rock, paper, and scissors
images = ['rock', 'paper', 'scissors']

# prompt the user to enter their selection and store it as an integer
user_selection = int(input('Type your selection:\n0: rock, 1: paper, 2: scissors\n>>> '))

# generate a random integer between 0 and 2 to represent the machine's selection
machine_selection = random.randint(0, 2)

# check if the user's selection is valid (between 0 and 2)
if user_selection > 2 or user_selection < 0:
    # if the selection is not valid, print an error message and exit the game
    print("You must use a value from 0 to 2. Exiting game.")
    exit()
else:
    # if the selection is valid, print the user's selection and the machine's selection
    print(f"user_selection: {user_selection}", images[user_selection])
    print(f"machine_selection: {machine_selection}", images[machine_selection])

    # determine the winner based on the game rules
    if user_selection == machine_selection:
        print(">> We have a tie")
    elif user_selection == 0 and machine_selection == 2:
        print(">> USER WINS")
    elif user_selection == 1 and machine_selection == 0:
        print(">> USER WINS")
    elif user_selection == 2 and machine_selection == 1:
        print(">> USER WINS")
    elif user_selection == 2 and machine_selection == 0:
        print(">> MACHINE WINS")
    elif user_selection == 0 and machine_selection == 1:
        print(">> MACHINE WINS")
    elif user_selection == 1 and machine_selection == 2:
        print(">> MACHINE WINS")
