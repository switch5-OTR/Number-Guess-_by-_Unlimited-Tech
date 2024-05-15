(#!/usr/bin/env python)
import random

# Set the number to be guessed
number_to_guess = random.randint(1, 10)

# Set the number of attempts
attempts = 0

# Set the maximum number of attempts
max_attempts = 5

# Game loop
while attempts < max_attempts:
    # Ask the user for their guess
    user_guess = int(input("Guess a number between 1 and 10: "))

    # Check if the user's guess is correct
    if user_guess == number_to_guess:
        print("Congratulations! You guessed the number correctly.")
        break
    elif user_guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    # Increment the number of attempts
    attempts += 1

# Check if the user ran out of attempts
if attempts == max_attempts:
    print("Sorry, you ran out of attempts. The number was " + str(number_to_guess))
