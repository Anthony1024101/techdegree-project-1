"""
Project 1 - Number Guessing Game
--------------------------------

"""

import random

print("Welcome to the Guessing Game!")


def start_game():
    
 Random_Number = random.randint(1,10)
 user_attempt = 1
 guess_number = 0
 while guess_number!= Random_Number:

  guess_number = input("What is the magic number?  ")
  try:
      guess_number = int(guess_number)
  
  except ValueError:
      print("please enter a correct number")
  
  else:
  
      if guess_number > Random_Number:
         print("It's lower. Total attempts: {}.".format(user_attempt)),
         user_attempt += 1
      elif guess_number < Random_Number:
         print("It's higher Total attempts: {}.".format(user_attempt)),
         user_attempt += 1
      elif guess_number == Random_Number:
         print(" You got it! Total attempts: {}.".format(user_attempt)),
        
 else:
        print("Game Over! Total tries {}.".format(user_attempt))
 return user_attempt


# Kick off the program by calling the start_game function.
start_game()
