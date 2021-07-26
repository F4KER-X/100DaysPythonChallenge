from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open(r"C:\Users\danny\Documents\GitHub\100DaysPythonChallenge\Day 020, 021 - Snake Game\data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(x=0, y=270)
        self.refresh_scoreboard()
        self.hideturtle()

    # increase score by 1
    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()

    # add the score
    def refresh_scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score {self.score} High Score: {self.high_score}",
            move=False, align="center")

    # print game over text
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"C:\Users\danny\Documents\GitHub\100DaysPythonChallenge\Day 020, 021 - Snake Game\data.txt", mode="w") as file2:
                file2.write(str(self.high_score))
        self.score = 0
        self.refresh_scoreboard()
