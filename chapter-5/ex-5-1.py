# Programming Exercise 5-1
#
# Program to convert kilometers to miles.
# This program accepts a distance in kilometers from the user,
# passes it to a function, which calculates its value in miles
# and displays the result for the user.


# Global constant for the ratio of kilometers to miles
miles_per_km = 1.60934

# define the main function
def main():
    
    # Define a local float variable to hold the distance in kilometers
    distance = 0.0
    # Get distance in kilometers from the user
    distance = float(input("Enter distance in KM: "))
    # pass the distance in kilometers to a function to convert to miles
    convert_km_to_miles(distance)


# define the function to convert to miles
# the function takes kilometers as an argument
# calculates the equivalent number of miles
# and prints the result
def convert_km_to_miles(distance_in_km):
    
    # Define a local float variable for miles
    distance_in_miles = 0.0
	# use the global conversion constant to compute miles    
    distance_in_miles = miles_per_km * distance_in_km
    # print the results, formatting float values to 2 decimal places
    formated_miles = format(distance_in_miles,'.2f')
    print("You have travled", formated_miles, "miles")

main()