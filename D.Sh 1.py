import random

options = ("rock", "paper", "scissor")
player = None
computer = random.choice(options)
while player not in options:
    player = input("enter a choice(rock, paper, scissor): ")

print(f"Player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("it's a tie1")
elif player == "rock" and computer == "scissor":
    print("you win!")
elif player == "paper" and computer == "rock":
    print("you win!")
elif player == "scissor" and computer == "paper":
    print('you win!')
else:
    print("you loose!")       
        
