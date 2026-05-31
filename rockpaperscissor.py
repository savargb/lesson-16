import random

while True:
    user_action = input("enter a choice:(rock,paper or scissor)")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nyou chose:{user_action} computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"both players selected the same option so its a tie.")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes scissors so you win")
        else:
            print("paper covers rock so you lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock so you win!")
        else:
            print("scissor cuts paper you lose.")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("scissor cuts paper so you win")
        else:
            print("rock smashes paper yuo lose")
    play_again = input("do you want to play again?(y/n): ")
    if play_again!="y":
        break

