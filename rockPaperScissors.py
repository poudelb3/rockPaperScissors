import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("type rock/paper/scissors To PLAY or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_pick = options[random_number]
    print("Computer picks", computer_pick + "." )

    if user_input == "rock" and computer_pick == "scissors":
        print("You won! Congratulations!!")
        user_score +=1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won! Congratulations!!")
        user_score +=1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won! Congratulations!!")
        user_score +=1
    else: 
        print("Ooops! You Lost.")
        computer_score +=1

print("You won", user_score, "times.")
print("Computer won", computer_score, "times.")
print("Goodbye!")
