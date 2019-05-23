import random
print("Rock...")
print("Paper.....")
print("Scissors.....")

players = input("Single or multiplayer? ").lower()
print("")
if (players == "single" or players == "s" or players == "1"):

	player1 = input("Opponent, make your move: ").lower()
	rand_num = random.randint(0,2)
	if rand_num == 0:
		player2 = "rock"
	elif rand_num == 1:
		player2 = "paper"
	else:
		player2 = "scissors"

	print(f"The computer chose: {player2}")

	if ((player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper")):
		print("✧･ﾟ: *✧･ﾟ:* YOU WIN! *:･ﾟ✧*:･ﾟ✧")

	elif ((player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper")):
		print("")
		print("      . ⋆ ˚｡⋆୨୧˚THE COMPUTER WINS!˚୨୧⋆｡˚ ⋆ .")
		print("")
		print("                                         ✧･ﾟ:* wow ᴵ’ᵐ ᵇᵉᵃᵘᵗᶦᶠᵘˡ *:･ﾟ✧*")
		print("")

	elif player1 == "gun":
		print("YOU WIN!")

	elif player1 == player2:
		print("It's a tie!")
	else:
		print("Invalid input. Please try again.")
         

elif players == "multi" or players == "m" or players == "multiplayer" or players == "2":

	player1 = input("Player 1, make your move: ").lower()

	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
	print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ NO CHEATING! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")


	player2 = input("Player 2, make your move: ").lower()

	if ((player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper")):
		print("Player 1 wins!")

	elif ((player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper")):
		print("Player 2 wins!")

	elif player1 == player2:
		print("It's a tie!")

	else:
		print("Invalid input. Please try again.")
else:
		print("Invalid input. Please try again.")