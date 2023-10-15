"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import random


def start_game():
    
   ### Intro Message ###
   print("Hello! Welcome to the number guessing game!")

   ### Create a Random Number ###

   ran_num = random.randint(1, 10)
   total_guesses = 0
   ### Loop to ask for a number and evaluate the answer given ###
   while True:
       try:
           num_guess = int(input("Try to guess the correct number in between one and 10 "))
           total_guesses += 1
       except ValueError:
            print("You did not enter a number")
            continue
       if num_guess < 1 or num_guess > 10:
            print("That number is not in the range of 1 to 10")
       elif num_guess == ran_num:
            print("{} is the correct number!".format(num_guess))
            print("It took you {} tries to get the correct number".format(total_guesses))
            return False
       elif num_guess > ran_num:
            print("The number is lower!")
       elif num_guess < ran_num:
            print("The number is higher!")
      
start_game()
    
    

