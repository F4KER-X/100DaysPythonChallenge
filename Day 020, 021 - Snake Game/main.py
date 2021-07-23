import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# screen commands (keys)
screen.listen()
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)
is_on = True


# while loop to keep the game running
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# when the head snake is on top of the food
    if snake.snake_list[0].distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# game over if game goes over the screen boarder
    if snake.snake_list[0].xcor() > 280 or snake.snake_list[0].xcor() < -280 \
        or snake.snake_list[0].ycor() > 280 or \
            snake.snake_list[0].ycor() < -280:
        is_on = False
        scoreboard.game_over()


# game over if the snake collide with the tail
    for s in snake.snake_list[1:]:
        if snake.snake_list[0].distance(s) < 10:
            is_on = False
            scoreboard.game_over()

screen.exitonclick()
