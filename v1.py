print("Rock...")
print("Paper.....")
print("Scissors.....")

player1 = input("Player 1, make your move: ")

print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")
print("* * * * NO CHEATING * * * *")


player2 = input("Player 2, make your move: ")

if ((player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper")):
	print("Player 1 wins!")

elif ((player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper")):
	print("Player 2 wins!")

elif player1 == player2:
	print("It's a tie!")

else:
	print("Invalid input. Please try again.")