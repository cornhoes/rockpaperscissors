import random
print("Rock...")
print("Paper.....")
print("Scissors.....")

player1 = input("Opponent, make your move: ")
rand_num = random.randint(0,2)
if rand_num == 0:
	player2 = "rock"
elif rand_num == 1:
	player2 = "paper"
else:
	player2 = "scissors"

print(f"The computer chose: {player2}")


if ((player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper")):
	print("You win!")

elif ((player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper")):
	print("The computer wins!")

elif player1 == player2:
	print("It's a tie!")

else:
	print("Invalid input. Please try again.")