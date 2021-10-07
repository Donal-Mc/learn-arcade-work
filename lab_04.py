# Lab 04: Camel game
import random

# Introduction
print("Welcome to Zombie Night!!")
print("You are one of the last survivors of humanity, trying to reach Sanctuary.")
print("Atop your trusty Motorbike with nothing more than a flask of water you must")
print("outrun the horde and earn your safety.")
print()

# Variables for game
done = False
milesTraveled = 0
zombiesTraveled = -20
motorbikeFuel = 8
thirst = 0
flask = 3
SupplyCache = -1
# Game loop
while not done:

    # Choices
    print("A. Swig from flask.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Refuel at petrol station.")
    print("E. Status check.")
    print("Q. Quit.")
    print()

    # User's input
    userInput = input("What will you do? ")

    # Lets people quit
    if userInput.upper() == "Q":
        done = True
    # Status check
    elif userInput.upper() == "E":
        print("Miles traveled:", milesTraveled)
        print("Drinks in flask:", flask)
        print("Motorbike fuel levels:", motorbikeFuel)
        print("Thirst:", thirst)
        print("The zombies are", milesTraveled - zombiesTraveled, "miles behind you.")
        print()
    # refuelling the Bike
    elif userInput.upper() == "D":
        print("You pull up in an isolated petrol station and refuel.")
        print("Your bike is refuelled.")
        print("The Zombies relentlessly pursue you.")
        print()
        motorbikeFuel = 8
        zombiesTraveled += random.randrange(7, 15)
    # full speed ahead
    elif userInput.upper() == "C":
        miles = random.randrange(10, 21)
        milesTraveled += miles
        thirst += 1
        motorbikeFuel -= random.randrange(1, 3)
        zombiesTraveled += random.randrange(7, 15)
        SupplyCache = random.randrange(20)
        if SupplyCache == 10:
            thirst = 0
            motorbikeFuel = 8
            canteen = 3
            print("As you travel you find a seemingly abandoned building filled with supplies!")
            print("You fill your flask, whilst drinking as much as you can and")
            print("Find fuel for your bike!")
            print("The Zombies continue the chase.")
            print()
        else:
            print("You push onward at full speed, moving a total of", miles, "miles")
            print("Your thirst increases.")
            print("The Zombies continue the chase.")
            print()
    # moderate speed ahead
    elif userInput.upper() == "B":
        miles = random.randrange(5, 13)
        milesTraveled += miles
        thirst += 1
        motorbikeFuel -= 1
        zombiesTraveled += random.randrange(7, 15)
        SupplyCache = random.randrange(20)
        if SupplyCache == 10:
            thirst = 0
            motorbikeFuel = 8
            canteen = 3
            print("As you travel you find a seemingly abandoned building filled with supplies!")
            print("You fill your flask, whilst drinking as much as you can and")
            print("Find fuel for your bike!")
            print("The Zombies continue the chase.")
            print()
        else:
            print("You move forward, moving a total of", miles, "miles")
            print("Your thirst increases.")
            print("The Zombies continue the chase.")
            print()
    # Swig from flask
    elif userInput.upper() == "A":
        if flask > 0:
            flask -= 1
            thirst = 0
            print("You take a swig of your flask")
            print("You feel refreshed and energised")
        else:
            print("Your flask is empty. You regret every drop you ever wasted.")

    # Status updates
    # Thirst
    if thirst > 5:
        print("You died of dehydration!")
        print("Game Over.")
        print()
        done = True
    elif thirst > 4:
        print("You are thirsty!")
    # Distance traveled / win check
    if milesTraveled >= 200:
        print("Congratulations! You have reached Sanctuary and secured your safety!")
        print("You win!!!")
        print()
        done = True
    # Motorbike's fuel
    if motorbikeFuel <= 0:
        print("Your bike has run out of fuel!")
        print("With no bike, the zombies catch up to you and infect you")
        print("turning you into one of them.")
        print("Game Over.")
        print()
        done = True
    elif motorbikeFuel <= 3:
        print("Your bike is running low on fuel")
        print()
    # Zombie Horde's distance from you
    if milesTraveled - zombiesTraveled <= 0:
        print("The zombies have caught up with you!")
        print("They drag you into their horde turning you into one of them.")
        print("Game Over.")
        print()
        done = True
    elif milesTraveled - zombiesTraveled < 15:
        print("You see faint shapes on the horizon shambling towards you.")
        print("The zombies are advancing!")
        print()

# Exit message
print("Exiting Game. Play again sometime!!! .")
input("")