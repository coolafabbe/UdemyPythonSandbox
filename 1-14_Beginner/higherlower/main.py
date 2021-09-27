import os
import random as r
from arthigherlower import logo
from arthigherlower import vs
import game_data


def choose_data():
    data = r.choice(game_data.data)
    game_data.data.remove(data)
    return data


def print_compare(compare):
    return f'{compare["name"]}, a {compare["description"]} from {compare["country"]}'


def compare_data(data_a, data_b):
    if data_a["follower_count"] >= data_b["follower_count"]:
        return "a"
    else:
        return "b"


def higher_lower_game():
    os.system("cls||clear")
    print(logo)

    compare_a = choose_data()
    print("Compare A: " + print_compare(compare_a))
    print(vs)

    score = 0
    game_over = False
    while not game_over and len(game_data.data) > 0:
        compare_b = choose_data()
        while compare_a["name"] == compare_b["name"]:
            compare_b = choose_data()

        print("Against B: " + print_compare(compare_b))

        right_choice = compare_data(compare_a, compare_b)
        print(right_choice)

        user_choice = input("Who has more followers, type 'A' or 'B'\n").lower()
        if user_choice == right_choice:
            score += 1
            if True:  # user_choice == "b":
                compare_a = compare_b
            os.system("cls||clear")
            print(logo)
            print(f"You're right! Current score: {score}.")
            print("Compare A: " + print_compare(compare_a))
            print(vs)
        else:
            os.system("cls||clear")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = True

    if len(game_data.data) == 0:
        os.system("cls||clear")
        print(logo)
        print(f"You won, there are no more data to compare. Final score: {score}.")


higher_lower_game()
