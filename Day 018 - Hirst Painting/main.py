import random
from turtle import Turtle, Screen

# colors = colorgram.extract('image.jpg', 30)
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r,b,g)
#     colors_list.append(new_color)
#
# print(colors_list)

colors = [(149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31), (134, 184, 163), (197, 73, 92),
          (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), (232, 165, 176), (160, 158, 142), (54, 50, 45),
          (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), (147, 19, 17), (27, 102, 68),
          (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99)]


turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.penup()
turtle.hideturtle()
turtle.speed('fastest')
x_pos = -300
y_pos = -300
turtle.goto(x_pos, y_pos)
number_of_dot_per_line = 10
for i in range(1, number_of_dot_per_line + 1):
    for _ in range(number_of_dot_per_line):
        turtle.dot(20, random.choice(colors))
        turtle.penup()
        turtle.forward(50)
    turtle.goto(x_pos, (y_pos + (i * 50)))

screen.exitonclick()
