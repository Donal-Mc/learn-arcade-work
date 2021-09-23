done = False

while not done:
    quit = input("Do you want to quit? ")
    if quit.lower() == "y":
        done = True
        print("Bye!")
        continue

    attack = input("Do you want to attack the dragon? ")
    if attack.lower() == "y":
        done = True
        print("Bad choice, you died!")