from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FONT2 = ("Press Start 2P", 20, "normal")


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