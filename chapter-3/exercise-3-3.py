# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.
numerical_age = float(input("What is your age?: "))
# Get the person's age.
# remember to convert the input to an int.
# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.
if numerical_age < 2:
    print("You are an Infant")
elif numerical_age > 2 and numerical_age < 12:
    print("You are a Child")
elif numerical_age > 12 and numerical_age < 18:
    print("You are a Teen")
elif numerical_age > 18:
    print("You are an Adult")
# display a message with the age category.



