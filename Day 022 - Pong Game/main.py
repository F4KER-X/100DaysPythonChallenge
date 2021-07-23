from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

is_on = True
sleep_timer = 0.1

while is_on:
    time.sleep(sleep_timer)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(
            left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep_timer *= 0.9
        print(sleep_timer)

    if ball.xcor() > 380:
        ball.reset_position()
        sleep_timer = 0.1
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        sleep_timer = 0.1
        scoreboard.r_point()


screen.exitonclick()
