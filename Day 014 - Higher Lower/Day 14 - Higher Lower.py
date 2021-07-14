from art import logo, vs
from game_data import data
import os
import random


def clear():
    return os.system('cls')


clear()
print(logo)
counter = 0
is_game_over = False
compare_b = random.choice(data)


while not is_game_over:
    compare_a = compare_b
    compare_b = random.choice(data)

    while compare_a == compare_b:
        compare_b = random.choice(data)

    print(
        f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")

    print(vs)

    print(
        f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a':
        if compare_a['follower_count'] >= compare_b['follower_count']:
            counter += 1
            clear()
            print(logo)
            print(f"You are right! Current score {counter}")
        else:
            is_game_over = True
            clear()
            print(f"Sorry, that's wrong. Final score: {counter}")
    elif answer == 'b':
        if compare_a['follower_count'] <= compare_b['follower_count']:
            counter += 1
            clear()
            print(logo)
            print(f"You are right! Current score {counter}")
        else:
            is_game_over = True
            clear()
            print(f"Sorry, that's wrong. Final score: {counter}")
