from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(x=0, y=270)
        self.refresh_scoreboard()
        self.hideturtle()

    # increase score by 1
    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_scoreboard()

    # add the score
    def refresh_scoreboard(self):
        self.write(arg=f"Score {self.score}", move=False, align="center")

    # print game over text
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center')
