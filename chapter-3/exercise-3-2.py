# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats


# Get length A from the user and convert it to a float
length_A = float(input("What is the length of rectangle A: "))
# Get width A from the user and convert it to a float
width_A = float(input("What is the width of rectangle A: "))
# Get length B from the user and convert it to a float
length_B = float(input("What is the length of rectangle B: "))
# Get width B from the user and convert it to a float
width_B = float(input("What is the width of rectangle B: "))
# Calculate area A
area_A = length_A * width_A
area_A = ("%.2f" % area_A)
# Calculate area B
area_B = length_B * width_B
area_B = ("%.2f" % area_B)
# Print each area, formatting the values to 2 decimal places
print("Area A is", area_A)
print("Area B is", area_B)
# if area A is greater, print "A is greater" message.
if area_A > area_B:
    print("A is greater")
# else if area B is greater, print "B is greater" message.
elif area_B > area_A:
    print("B is greater")
# else print "A and B are equal" message.
elif area_A == area_B:
    print("A and B are equal")
