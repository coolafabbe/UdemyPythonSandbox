from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0,260)
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        text = f"Score = {self.score}"
        self.write(arg=text, move=False, align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.clear()
        text = f"Game over! Score = {self.score}"
        self.write(arg=text, move=False, align="center", font=("Arial", 20, "normal"))

    # def game_over(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #     self.score = 0