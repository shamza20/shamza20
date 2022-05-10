from random import choice
objects = ["Rock","Paper","Scissors"]
computer = choice(objects)
rps = input("What will you choose? Rock,Paper,Scissors ?")
if rps == computer:
        print("It is a tie!")
if rps == ("Rock"):
    if computer == ("Scissors"):
        print("You Won !")
if rps == ("Paper"):
    if computer == ("Rock"):
        print("You won !")
if rps == ("Scissors"):
    if computer == ("Paper"):
        print("You Won !")
if computer == ("Scissors"):
    if rps == ("Paper"):
        print("You lost !")
if computer == ("Rock"):
    if rps == ("Scissors"):
        print("You lost !")
if computer == ("Paper"):
    if rps == ("Rock"):
        print("You lost !")
print("Thanks for Playing")
