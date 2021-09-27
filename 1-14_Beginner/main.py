# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bmi = round(weight / (height ** 2))

# if bmi < 18.5:
#     result = "you are underweight"
# elif bmi < 25:
#     result = "you have a normal weight."
# elif bmi < 30:
#     result = "you are slightly overweight."
# elif bmi < 35:
#     result = "you are obese."
# else:
#     result = "you are clinically obese."

# print(f"Your BMI is {bmi}, ",'\033[1m' + result,'\033[0m')

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# name = name1.lower() + name2.lower()

# word1 = "true"
# word2 = "love"

# sum = 0

# for item in word1:
#     sum += name.count(item) * 10

# for item in word2:
#     sum += name.count(item)

# if sum < 10 or sum > 90:
#     print(f"Your score is {sum}, you go together like coke and mentos.")
# elif sum >= 40 and sum <= 50:
#     print(f"Your score is {sum}, you are alright together.")
# else:
#     print(f"Your score is {sum}.")



# if random.randint(1, 2) == 1:
#     print("Heads")
# else:
#     print("Tails")

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# import random

# print(f"{names[random.randint(0, len(names) -1)]} is going to buy the meal today!")

# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# values = [rock, paper, scissors]

# user = int(input("What do you choose? Type 0 for Rock, 1, for Paper or 2 for Scissors.\n"))
# comp = random.randint(0,2)

# if user >= 0 and user <= 2:
#     print(values[user])
#     print("Computer choose:")
#     print(values[comp])

#     if comp == user:
#         print("Draw")
#     elif comp == user + 1 or comp == 0:
#         print("You loose!")
#     else:  
#         print("You Win!")
# else:
#     print("You entered an invalid number, you loose!")

# ## Chapter 50 High score
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# max_value = 0
# for item in student_scores:
#     if item > max_value:
#         max_value = item

# print(max_value)
# #print(max(student_scores))

# sum = 0
# for item in range(2,101, 2):
#     #if item % 2 == 0:
#     sum += item

# print(sum)

# for item in range (1, 101):
#     output = ""
#     if item % 3 == 0:
#         output+= "Fizz"
#     if item % 5 == 0:
#         output+= "Buzz"
#     if output == "":
#         output = item #str(item)
#     print(output)

# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = []

# for letter in range (0, nr_letters):
#     password.append(random.choice(letters))
# for symbol in range (0, nr_symbols):
#     password.append(random.choice(symbols))
# for number in range (0, nr_numbers):
#     password.append(random.choice(numbers))

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# random.shuffle(password)
# password = "".join(password)

# print(password)


# import math

# def printPi():
#     print(math.pi)

# printPi()    

# def greet(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     return True

# print(type(greet("Fabian")))

# Parameter - def greet(name) - name is the parameter.
# Argument - greet("Fabian") - "Fabian" is the argument.

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Fabian", "Blikstorp") # positional argument
# greet_with(name = "Fabian", location = "Blikstorp") # Keyword arguments.

# #Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#     num_of_cans = math.ceil((height * width / cover))
#     print(f"You'll need {num_of_cans} cans of paint.")

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# #Write your code below this line 👇
# def prime_checker(number):
#     prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             prime = False

#     if prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         if letter in alphabet:
#             index = alphabet.index(letter) + shift
            
#             if index >= len(alphabet):
#                 index -= len(alphabet)

#             cipher_text += alphabet[index]
#         else:
#             print(f"You've entered an invalid letter ({letter})")
#             quit()
#     print(f"The encrypted text is {cipher_text}")

# def decrypt(text, shift):
#     plain_text = ''
#     for letter in text:
#         if letter in alphabet:
#             index = alphabet.index(letter) - shift

#             if index < 0:
#                 index += len(alphabet)

#             plain_text += alphabet[index]
#         else:
#             print(f"You've entered an invalid letter ({letter})")
#             quit()
#     print(f"The encoded text is {plain_text}")

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""

#     shift_amount = shift_amount % len(alphabet)

#     if cipher_direction == "decode":
#         shift_amount *= -1

#     for letter in start_text:
#         if letter in alphabet:
#             index = alphabet.index(letter) + shift_amount

#             if index >= len(alphabet):
#                 index -= len(alphabet)
#             elif index < 0:
#                 index += len(alphabet)

#             end_text += alphabet[index]
#         else: 
#             end_text += letter

#     print(f"The {cipher_direction}d text is {end_text}")

# caesar(text, shift, direction)

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     grade = ""
#     score = student_scores[key] 
#     if score > 90 and score <= 100:
#         grade = "Outstanding"
#     elif score > 80 and score <= 90:
#         grade = "Exceeds Expectations"
#     elif score > 70 and score <= 80:
#         grade = "Acceptable"
#     elif score <= 70:
#         grade = "Fail"
    
#     student_grades[key] = grade

# # 🚨 Don't change the code below 👇
# print(student_grades)

# import os
# #os.system('cls||clear')

# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''

# os.system('cls||clear')
# print(logo)

# auction = {}

# should_continue = True
# while should_continue:
#     name = input("What is your name?\n")
#     bid = int(input("What's your bid price?\n"))
    
#     auction[name] = bid

#     cont = input("Are there more users? (yes or no)\n").lower()
#     if cont == "no":
#         should_continue = False
#     else:
#         os.system('cls||clear')

# highest_bidder = ""
# highest_bid = 0
# for key in auction:
#     if auction[key] > highest_bid:
#         highest_bidder = key
#         highest_bid = auction[key]

# print(f"Highest bidder was {highest_bidder} with a bid on ${highest_bid}")
# print(auction)

