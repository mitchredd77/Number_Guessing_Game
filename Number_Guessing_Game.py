"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import random

def start_game():
    
### print out intro message
   print("Hello! Welcome to the number guessing game!")

### Create a Random Number and  hold it's value
   ran_num = random.randint(1, 10)
   total_guesses = 0
   scores = []
     
### While loop to ask for a number and evaluate the answer given
   while True:
       try:
          num_guess = int(input("\nTry to guess the correct number in between 1 and 10 "))
          total_guesses += 1
          
### Handle guesses that are floats or non-integer
       except ValueError:
          print("\nThat is not an exact number of 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10!")
          continue
         
### If there is any other exception, ask for a new guess
       except:
          print("\nThere was an error with your guess, please try again.")
          continue
          
### When answer is correct, add score to scores list, and ask if they would like to play again
       if num_guess == ran_num:
            print("\n{} is the correct number!".format(num_guess))
            print("\nIt took you {} tries to get the correct number".format(total_guesses))
            scores.append(total_guesses)
            best_score = min(scores)
            play_again = input("\nWould you like to play again? (yes or no) ").lower()
            if play_again == "yes":
                print("\nYour current lowest amount of guesses to get the correct number is {}".format(best_score))
                ran_num = random.randint(1, 10)
                total_guesses = 0
            else:
                print("\nYour best score was {} guesses. Goodbye and have a great day!".format(best_score))
                return False
               
### If the number was less than 1 or greater than 10
       elif num_guess < 1 or num_guess > 10:
            print("{} is not a number between 1 and 10".format(num_guess))
            
### Feedback on whether the guess is low or high
       elif num_guess > ran_num:
            print("It's lower!")
       elif num_guess < ran_num:
            print("It's higher!")
      
start_game()
    
    

