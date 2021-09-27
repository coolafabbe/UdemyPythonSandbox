import os
import random as r
from art import guess_logo

should_continue = True
while should_continue:
    os.system("cls||clear")
    print(guess_logo)
    print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100")
    choosen_number = r.randint(1,100)
    print("psst, correct number is " + str(choosen_number))
    difficulty = input("choose a difficulty. type 'easy' or 'hard':  ").lower()
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Wrong entery, game closes.")
        should_continue = False
    
    game_over = False
    while attempts > 0 and not game_over:
        print(F"you have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        attempts -= 1

        if guess == choosen_number:
            print(f"You got it! The answer was {choosen_number}")
            game_over = True
        elif guess < choosen_number:
            print("Too low.")
        elif guess > choosen_number:
            print("Too high.")

        if not game_over and attempts > 0:
            print("Guess again.")
        else:
            print("Game over.")
            should_continue = input("Do you want to play again? (y or n)").lower() == "y"

        