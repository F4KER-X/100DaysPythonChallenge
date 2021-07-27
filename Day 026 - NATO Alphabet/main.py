import pandas
FILE_LOCATION = "Day 025 - U.S. State Game\50_states.csv"
data = pandas.read_csv(FILE_LOCATION)


list_dict = {row.letter: row.code for index, row in data.iterrows()}


user_input = input("Enter a word: ").upper()


letter_list = [letter for letter in user_input]

final_list = [list_dict[letter] for letter in letter_list]

print(final_list)
