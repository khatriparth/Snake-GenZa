from turtle import Turtle
import random

X1 = -250
Y1 = 250

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.show_food()
        
    def show_food(self):
        self.shape("circle")
        self.color("green")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        self.goto(random.randint(X1, Y1), random.randint(X1, Y1))
        
    def move_food(self):
        self.goto(random.randint(X1, Y1), random.randint(X1, Y1))
