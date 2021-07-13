import random
from art import logo


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return 10
    else:
        return 5


def compare(guess, user, attempts):
    if guess == user:
        print((f"You got it! The answer was {guess}."))
    elif guess > user:
        return attempts - 1
        print("Too low")
    elif guess < user:
        print("Too High")
        return attempts - 1


def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()
    guess_number = random.randint(1, 101)
    user_input = 0
    while user_input != guess_number:

        print(f"you have {attempts}")
        user_input = int(input("Your guess: "))

        attempts = compare(guess_number, user_input, attempts)

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess_number != user_input:
            print("Guess again.")


game()
