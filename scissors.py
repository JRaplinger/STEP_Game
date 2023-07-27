import random
print("Welcome to rock paper scissors")
choices=("rock", "paper", "scissors")
playerwin=0
computerwin=0

while True:
    playerchoices =input("Enter your choice: Rock, Scissors, Paper").lower()
    if playerchoices not in choices:
        print("Not in choices")
        continue

    computer = random.choice(choices)
    if playerchoices==computer:
        print("Its a tie")
        continue
    elif playerchoices=="rock" and computer=="scissors" or playerchoices== "scissors" and computer=="paper" or playerchoices=="paper" and computer=="rock":
        print("You win")
        playerwin+=1
        continue    
    else:
        print("You lose")
        computerwin+=1
        continue
