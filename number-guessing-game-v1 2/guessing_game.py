"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random
# Create the start_game function.
def start_game():
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
  print("Hello, Welcome to The Number Guessing Game")
#   2. Store a random number as the answer/solution.
  random_number = random.randint(1, 10)
  guessed_number = 0
  guesses = 0
#   3. Continuously prompt the player for a guess.
  while True:
    try:
        guess = input("Guess a number between 1 and 10: ")
        guesses += 1
        
        while True:
          try:
            guessed_number = int(guess)
            break
          except ValueError:
            print("Please input numbers only.")
            guess = input("Guess a number between 1 and 10: ")
#     a. If the guess is greater than the solution, display to the player "It's lower".
        if 1 <= guessed_number <= 10:
          if guessed_number > random_number:
            print("It's lower")
#     b. If the guess is less than the solution, display to the player "It's higher".
          elif guessed_number < random_number:
            print("It's higher")
#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
          else:
            print(f"You're correct! It took {guesses} guesses")
            print("The game is over")
            break
        else:
          raise ValueError("Please enter a number between 1 and 10")
          
    except ValueError as e:
      print(e)
# ( You can add more features/enhancements if you'd like to. )
# Kick off the program by calling the start_game function.
start_game()
