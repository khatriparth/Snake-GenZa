from turtle import Turtle
import json

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FONT2 = ("Press Start 2P", 20, "normal")
FONT3 = ("Press Start 2P", 10, "normal")

FILE_PATH = "/home/parth/PycharmProjects/PythonProject/Games/Snake/highscores.json"
HIGHSCORES = []


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(220, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT2)
        self.goto(0, -20)
        self.write("Press Escape to Exit", align="center", font=FONT3)
        
    def is_high_score(self):
        
        with open("FILE_PATH" "r") as f:
            data = json.load(f)

        for i in range(len(data)):
            HIGHSCORES.append(data[f"Highscore{i + 1}"])

        return True