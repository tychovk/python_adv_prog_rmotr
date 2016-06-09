"""
Write a program that generates a secret random number and asks the user to guess it.
It should count how many attempts were made before the number is guessed.
The program must also give hints to the user.
Example:
    python guess_a_number.py
    > Guess your number
    > 3
    > Wrong! Try with a larger one
    > 5
    > Wrong! Try with a smaller one
    > 4
    > You guessed correctly! The number was 4 indeed!
"""

import random

def guess_a_number(to_guess = False, try_guess = False, message = "Guess your number"):
    if to_guess == False:
        to_guess = random.randint(0,10)
    
    try_guess = input(message)
    
    if isinstance(try_guess, str) and try_guess.isdigit():
        try_guess = int(try_guess)
    elif isinstance(try_guess, str):
        message = "That's not a number. Give me a number!"
        return guess_a_number(to_guess, False, message)
    
    if try_guess > to_guess:
        message = ("Wrong! Try with a smaller one")
        return guess_a_number(to_guess, try_guess, message)
    if try_guess < to_guess:
        message = "Wrong! Try with a larger one"
        return guess_a_number(to_guess, try_guess, message)
    else:
        return "You guessed correctly! The number was indeed!"
        
    
        
print (guess_a_number())