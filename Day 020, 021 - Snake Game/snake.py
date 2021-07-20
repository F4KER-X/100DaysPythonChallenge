from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POS = 20
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()

    # create the snake
    def create_snake(self):
        for position in POSITIONS:
            self.add_snake(position)

    # moving the snakes together
    def move(self):
        for snake in range(len(self.snake_list) - 1, 0, -1):
            x = self.snake_list[snake - 1].xcor()
            y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(x=x, y=y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    # UP key
    def move_up(self):
        if self.snake_list[0].heading() != 270:
            self.snake_list[0].setheading(90)

    # DOWN key
    def move_down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)

    # LEFT key
    def move_left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)

    # RIGHT key
    def move_right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)

    # add a new snake
    def extend(self):
        self.add_snake(self.snake_list[-1].position())

    # main function for creating a snake
    def add_snake(self, position):
        new_snake = Turtle('square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.goto(position)
        self.snake_list.append(new_snake)
