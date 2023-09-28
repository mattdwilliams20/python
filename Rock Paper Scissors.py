import random
computer_score = 0
player_score = 0

options = ["rock", "paper", "scissors"]

while True:
    command = input("Choose rock, paper, scissors or type Q to quit. ").lower()
    if command == "q":
        break

    if command not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if command == options[0] and computer_pick == options[2]:
        print("You won!")
        player_score += 1
        print("Player Score:",player_score)
        print("Computer Score:", computer_score)
    elif command == options[1] and computer_pick == options[0]:
        print("You won!")
        player_score += 1
        print("Player Score:", player_score)
        print("Computer Score:", computer_score)
    elif command == options[2] and computer_pick == options[1]:
        print("You won!")
        player_score += 1
        print("Player Score:", player_score)
        print("Computer Score:", computer_score)
    elif command == options[2] and computer_pick == options[2]:
        print("Tie. Try Again!")
        player_score += 0
        print("Player Score:", player_score)
        print("Computer Score:", computer_score)
    elif command == options[1] and computer_pick == options[1]:
        print("Tie. Try Again!")
        player_score += 0
        print("Player Score:", player_score)
        print("Computer Score:", computer_score)
    elif command == options[0] and computer_pick == options[0]:
        print("Tie. Try Again!")
        player_score += 0
        print("Player Score:", player_score)
        print("Computer Score:", computer_score)
    else:
        print("You lost!")
        computer_score += 1
        print("Player Score:", player_score)
        print("Computer Score:", computer_score)

print("You won", player_score, "times.")
print("Computer won", computer_score, "times.")
if player_score > computer_score:
    print("Player wins.")
if computer_score > player_score:
    print("Computer wins.")
if computer_score == player_score:
    print("Overall tie. Run it back.")
print("Thanks for playing!")



















