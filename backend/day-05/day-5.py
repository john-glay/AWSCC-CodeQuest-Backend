print("\nOPTIONS")
print("• rock")
print("• paper")
print("• scissors\n")

p1 = input("PLAYER #1: ").lower()

import random
options = ["rock", "paper", "scissors"]
p2 = random.choice(options)
print(f"PLAYER #2: {p2}")

if (p1 == 'rock') or (p1 == 'paper') or (p1 == 'scissors'): 

    if p1 != p2:
        if (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
            print("\nPlayer #1 Wins!\n")
        else:
            print("\nPlayer #2 Wins!\n")
    else:
        print("\nIt's a draw!\n")

else:
    print("\nInputs must be rock, paper, and scissors only\n")
