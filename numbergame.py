import random
playing = True
number = int(random.randint(0,9))

print("I will generate a number and you have to guess it one digit at a time.")
print("The game ends once you get the number correct")
while playing:
    guess = int(input("Give me your best guess! \n"))
    if number == guess:
        print("you win the the game!")
        print("The number was ",number)
        break
    else:
        print("Thats not right , try  again. \n")