# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# https://waitbutwhy.com/2014/05/life-weeks.html
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

age = int(input("Enter your age and I'll tell you how much days, week and months you still have till turning 70 years old\n"))

months_left = 90*12 - age*12
weeks_left = 90*52 - age*52
days_left = 90*365 - age*365

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print (message)