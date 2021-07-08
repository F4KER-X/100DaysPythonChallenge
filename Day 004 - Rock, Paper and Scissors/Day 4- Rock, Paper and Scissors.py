import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]


user_input = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

cpu_choice = random.choice(options)
result = ""

if (user_input != '1' or user_input != '0' or user_input != '2'):
    print("Invalid input. You lose!")
    exit(0)

if (user_input == '0' and cpu_choice == rock) or \
    (user_input == '1' and cpu_choice == paper) or \
        (user_input == '2' and cpu_choice == scissors):
    result = "It's a tie"
elif (user_input == '0' and cpu_choice == paper) or \
    (user_input == '1' and cpu_choice == scissors) or \
        (user_input == '2' and cpu_choice == rock):
    result = "Computer wins. Game over"
else:
    result = "You win. Congratz"

print(options[int(user_input)])
print("Computer choice: ")
print(cpu_choice)
print(result)
