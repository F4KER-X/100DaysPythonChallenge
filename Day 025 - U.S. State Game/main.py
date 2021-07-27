import turtle
import pandas

# create the turtle screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = r"C:\Users\danny\Documents\GitHub\100DaysPythonChallenge\Day 025\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read the file
data = pandas.read_csv(
    r"C:\Users\danny\Documents\GitHub\100DaysPythonChallenge\Day 025\50_states.csv")

# while loop to keep the game running
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guessed States",
                              prompt="What's another state's name?").title()

    all_states = data['state'].to_list()
    if answer == 'Exit':
        break

    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer]
        t.goto(int(state_data['x']), int(state_data['y']))
        t.write(answer)
        guessed_states.append(answer)


# check the states that we guessed and remove them from the states list,
#  then create a new file with what we have left
# to make it easier, dict is better for reading
for state in guessed_states:
    all_states.remove(state)
state_dic = {
    "state": all_states
}
df = pandas.DataFrame(state_dic)
df.to_csv("states_to_learn.csv")
