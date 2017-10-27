#main
    #prompt
    #handle_choice
    #display
import circle
import rectangle

AREA_OF_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():

    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter your choice: "))
        output = handle_choice(choice)
        print(output)
        
def display_menu():
    print(" MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

def handle_area_of_cicle(AREA_OF_CIRCLE_CHOICE):
        radius = float(input("Enter the circle's radius: "))
        return "The area is" + " "  + str(circle.area(radius))

def handle_circumference_of_circle(CIRCUMFERENCE_CHOICE):
    radius = float(input("Enter the circle's radius: "))
    return "The circumference is" + " " + str(circle.circumference(radius))

def handle_area_of_rectangle(AREA_RECTANGLE_CHOICE):
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    return "The area is" + " "  + str(rectangle.area(width,length))

def handle_perimeter_of_rectangle(PERIMETER_RECTANGLE_CHOICE):
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    return "The perimeter is" + " "  + str(rectangle.perimeter(width,length))

def handle_choice(choice):
    if choice == AREA_OF_CIRCLE_CHOICE:
        return handle_area_of_cicle(AREA_OF_CIRCLE_CHOICE)
    elif choice == CIRCUMFERENCE_CHOICE:
       return handle_circumference_of_circle(CIRCUMFERENCE_CHOICE)
    elif choice == AREA_RECTANGLE_CHOICE:
       return handle_area_of_rectangle(AREA_RECTANGLE_CHOICE)
    elif choice == PERIMETER_RECTANGLE_CHOICE:
       return handle_perimeter_of_rectangle(PERIMETER_RECTANGLE_CHOICE)
    elif choice == QUIT_CHOICE:
        print("Exiting the program...")
    else:
        print("Error: Invalid selection.")

main()

