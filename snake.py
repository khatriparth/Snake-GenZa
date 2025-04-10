from turtle import Turtle
import random

COORDINATES = [(0, 0), (20, 0), (40, 0)] #starting coordinates of 3 blocks
CHAIN = []
STEP_DISTANCE = BLOCK_SIZE = 20 #to make the movement uniform
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
DIRECTION = random.choice([UP, DOWN, LEFT, RIGHT]) #to make the snake move in a random direction at the starting of the game
HEAD_COLOR = "blue"

class Snake:
    def __init__(self):
        self.chain = []
        self.create_snake()
        self.head = self.chain[0] # declaring head as the first element of the chain
        self.allow_collision = False

    def add_block(self, position):
        new_block = Turtle()
        new_block.shape("square")
        new_block.color("white")
        # new_block.shapesize(STEP_DISTANCE / 20)
        new_block.penup()
        new_block.goto(position)
        self.chain.append(new_block)

    def create_snake(self):
        for position in COORDINATES:
            self.add_block(position)

    def move_the_body(self):
        for block in range(len(self.chain) - 1, 0, -1):
            new_x_cor = self.chain[block - 1].xcor()
            new_y_cor = self.chain[block - 1].ycor()
            self.chain[block].goto(new_x_cor, new_y_cor)
        self.head.forward(STEP_DISTANCE)

    def extend_snake(self):
        self.add_block(self.chain[-1].position())

    def enable_collision(self):
        self.allow_collision = True

    def reset_snake(self):
        for block in self.chain:
            block.hideturtle()
        self.chain.clear()
        self.create_snake()
        self.head = self.chain[0]

# key controls
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
