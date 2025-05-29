import random

def guess_the_number():
	print("Welcome to the guessing game!")

	while True:
		secret_number = random.randint(1, 10)
		guess = int(input("Guess a number between 1 and 10: "))

		match guess:
			case _ if guess == secret_number:
				print("Congratulations, you guessed it!")
			case _ if guess > secret_number:
				print("Oops, your guess is a bit high, try again!")
			case _ if guess < secret_number:
				print("Nope, your guess is a bit too low, try again!")

		play_again = input("Do you want to play again? (yes/no): ").lower()
		if play_again not in ('yes', 'y'):
			print("Thanks for playing, see you next time")
			break

guess_the_number()
