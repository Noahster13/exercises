upper_limit = int(input("What do you want to go to?: "))

def check_numbers(x,y,z):
    print(x,y,z)
   
for x in range(upper_limit):
    for y in range(upper_limit):
        for z in range(upper_limit):
            check_numbers(x,y,z)
            