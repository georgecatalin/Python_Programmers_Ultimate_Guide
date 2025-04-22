repeat = True

while repeat:
    print("Food menu:")
    print("1.Pizza con tutto")
    print("2.Ice cream")
    print("3.Spaghetti")
    print("0.Exit")

    user_choice = int(input("Enter your humble food choice: "))

    if user_choice == 1:
        print("Pizza is great")
    elif user_choice == 2:
        print("Ice cream rulz")
    elif user_choice == 3:
        print("Im lovin Spaghetti")
    elif user_choice == 0:
        # break
        repeat = False
    else :
        print("I do not know what you wish")
else: # this executes immediately when jumping out of the while loop . when repeat = False
    print("Thank you, come again")