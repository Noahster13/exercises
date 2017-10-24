# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.
user_number = int(input("Give me an integer from 1 to 10. "))
# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.
# Get number from user and convert it to an int
# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.
if user_number == 1:
    print("I is the Roman Numeral for 1.")
elif user_number == 2:
     print("II is the Roman Numeral for 2.")
elif user_number == 3:
    print("III is the Roman Numeral for 3.")
elif user_number == 4:
    print("IV is the Roman Numeral for 4.")
elif user_number == 5:
    print("V is the Roman Numeral for 5.")
elif user_number == 6:
    print("VI is the Roman Numeral for 6.")
elif user_number == 7:
    print("VII is the Roman Numeral for 7.")
elif user_number == 8:
    print("VIII is the Roman Numeral for 8.")
elif user_number == 9:
    print("IX is the Roman Numeral for 9.")
elif user_number == 10:
    print("X is the Roman Numeral for 10.")
# use a final else to display an error if number is out of range.
else:
    print(" Error: Not an integer inbetween 1 and 10, please try again.")
# display the numeral on the screen.






