from turtle import Turtle
import json

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FONT2 = ("Press Start 2P", 20, "normal")
FONT3 = ("Press Start 2P", 10, "normal")

FILE_PATH = "/home/parth/PycharmProjects/PythonProject/Games/Snake/highscores.json"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(220, 260)
        self.hideturtle()
        self.update_score()
        self.high_scores = self.load_high_scores(FILE_PATH)

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
    
    @staticmethod
    def load_high_scores(file_path):
        try:
            # If the file doesn't exist, or if the JSON in the file is corrupted, catch the relevant exceptions and return an empty dictionary
            with open(FILE_PATH, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return an empty dictionary if the file doesn't exist or is corrupted
            return {}
        
    def is_high_score(self):
        for score, name in self.high_scores.items():
            if self.score > int(score):
                return True
    
    def update_high_scores(self, player_name, score):
        self.high_scores = self.load_high_scores(FILE_PATH)

        scores = [(name, int(score)) for name, score in self.high_scores.items()]
        scores.append((player_name, self.score))
        scores.sort(key=lambda x: x[1], reverse=True)
        scores = scores[:5]
        
        updated_high_scores = {score : name for score, name in scores}
        with open(FILE_PATH, "w") as score_file:
            score_file.write(json.dumps(updated_high_scores, indent = 4))
            
        if self.score >= scores[-1][1]:
            print("You got a new high score!")
        else:
            print("Scores updated.")
