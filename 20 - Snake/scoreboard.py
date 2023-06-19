from turtle import Turtle

# Scoreboard Globals
ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.shape()
        self.pu()
        self.goto(0, 280)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()


    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        print(self.high_score)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
