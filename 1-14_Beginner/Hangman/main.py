import random
import os

from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

os.system('cls||clear')

# choose word to be guessed
choosen_word = random.choice(word_list)
print(logo)
print(choosen_word)

# create guessed array
display = []
for item in choosen_word:
    display += "_"

lives = 6
while lives > 0 and "_" in display:
    # ask user to guess a letter
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha or len(guess) != 1:
        print("Faulty input, you loose! ")
        quit()

    if guess in choosen_word: #choosen_word.__contains__(letter): #.find(letter):
        print(f"You entered a valid letter, {guess}, congrats!")
        for i in range(len(choosen_word)):
            if choosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"You entered an invalid letter, {guess}, you loose a life.")
        lives -= 1

    print(f"{' '.join(display)}")
    print(stages[lives])


    if not "_" in display:
        print("You Win!")
    elif lives <= 0:
        print("You loose!")