# Instructions
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# loop through the numbers 1 to 99 (inclusive)
for number in range(1, 100):
    # check if the number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # check if the number is divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # check if the number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # if none of the above conditions are met, print the number
    else:
        print(number)