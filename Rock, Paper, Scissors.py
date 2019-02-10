import random
import time

# Score
playerScore = 0
computerScore = 0

while True:
	print("Rock, Paper, Scissors \n")

# Moves
	moves = ['ROCK', 'PAPER', 'SCISSORS']

# Get user choice.
	print("Please choose one; Rock, Paper or Scissors.\n")
	playerChoice = input().upper()

# Include catch if user did not type 'rock', 'paper' or 'scrissors'.
	while playerChoice not in moves:
		print("Invalid option. Make sure you type 'rock', 'paper' or 'scissors'.\n")
		playerChoice = input().upper()

	computerChoice = random.choice(moves)
                
	print("\nPlayer's Choice: ", playerChoice)
	print("Computer's Choice: ", computerChoice, "\n")

	if playerChoice  == computerChoice:
		print("The game is a draw. That was underwhelming.\n")
		playerScore += 0.5
		computerScore += 0.5

	elif playerChoice == "ROCK" and computerChoice == "PAPER":
		print("Hard luck. You lost :(.\n")
		computerScore += 1

	elif playerChoice == "ROCK" and computerChoice == "SCISSORS":
		print("Well done you won! :).\n")
		playerScore += 1

	elif playerChoice == "PAPER" and computerChoice == "ROCK":
		print("Well done you won! :).\n")
		playerScore += 1

	elif playerChoice == "PAPER" and computerChoice == "SCISSORS":
		print("Hard luck. You lost :(.\n")
		computerScore += 1

	elif playerChoice == "SCISSORS" and computerChoice == "ROCK":
		print("Hard luck. You lost :(.\n")
		computerScore += 1

	elif playerChoice == "SCISSORS" and computerChoice == "PAPER":
		print("Well done you won! :).\n")
		playerScore += 1

# End of game.

	time.sleep(3)

# Score tally.
	print("\nThe current score is: \n")
	print("Your score is: ", playerScore)
	print("Computer score is: ", computerScore, "\n")

	if playerScore > computerScore:
		print("Congrats! You are in the lead.\n")

	if playerScore < computerScore:
		print("Oh dear! Computer is in the lead.\n")

	time.sleep(3)

# Ask user if they want to play again.
	print("\nDo you want to play again? Yes or No.\n")
	playAgain = input().upper()
	if playAgain == "NO":
		print("\nGame Over.\n\n")
		break
	else:
		print("\nNew Game.\n\n")
		continue