# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats


# Constant for the number of square feet in an acre.


# Get the square feet in the tract from the user.
# you will need to convert this input to a float


# Calculate the number of acres.


# Print the number of acres.
# remember to format the acres to two decimal places

square_feet = input("How many square feet?: ")
square_feet_to_acre_ratio = float(2.2957e-5)
acre = square_feet * square_feet_to_acre_ratio
rounded_acre = ("%.2f" % acre)
print(acre)

