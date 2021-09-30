import arcade
def main():
    """This is my main program function"""
    print("Welcome to Zombie Night!!! ")
    print("You are running from an undead horde, trying to get to Sanctuary. ")
    print("With your motorbike and flask you must escape the horde")
    print("and secure your safety")

    done = False

    while not done:
        print("A. Drink from flask. ")
        print("B. Ahead moderate speed")
        print("C. Ahead full speed")
        print("D. Camp for the night")
        print("E. Check yourself")
        print("F. Quit")

        user_input = input("What is your choice? ")
        if user_input.lower() == "q":
            print("Come back soon. ")
            done = True


main()