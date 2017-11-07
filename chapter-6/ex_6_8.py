def main():
    valid_number = False
    while not valid_number:
        user_input = ""
        user_input = input("Please enter a integer between 1 and 10: ")
        try:
            int(user_input)
            valid_number = True
        except ValueError:
            print(user_input, "is not a valid number")
        if user_input < 1:
            print("Your number is too small.")
        elif user_input > 10:
            print("Your number is too large.")
        else:
            valid_number = True
            
    print("Thank You, your number is", user_input)    

main()