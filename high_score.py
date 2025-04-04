import json

FILE_PATH = "/home/parth/PycharmProjects/PythonProject/Games/Snake/highscores.json"
HIGHSCORES = []


with open('FILE_PATH' "r") as f:
    data = json.load(f)

for i in range(len(data)):
    HIGHSCORES.append(data[f"Highscore{i + 1}"])

print(HIGHSCORES)