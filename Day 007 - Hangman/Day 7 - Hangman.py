import random
import hangman_art
import hangman_word

print(hangman_art.logo)

chosen_word = random.choice(hangman_word.word_list)
word_length = len(chosen_word)


empty_list = []
for _ in range(word_length):
    empty_list.append("_")

lives = 6

game_over = False

while not game_over:

    guess = input("Guess a letter: ").lower()

    if guess in empty_list:
        print(f"You've already guessed {guess}")

    for position in range(word_length):

        if guess == chosen_word[position]:
            empty_list[position] = chosen_word[position]

    print(" ".join(empty_list))

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in empty_list:
        game_over = True
        print("You win")

    print(hangman_art.stages[lives])
