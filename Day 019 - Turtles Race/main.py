from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles_list = []
is_game_on = False

i = 1
for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    i += 1
    turtle.penup()
    turtle.goto(x=-230, y=(-225+(i*50)))
    turtles_list.append(turtle)

if user_input:
    is_game_on = True


while is_game_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_input:
                print(
                    f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_turtle} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
