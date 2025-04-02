from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()

screen.tracer(0)
screen.title("Snake GenZa")
screen.bgcolor("black")
screen.setup(width=600, height=600)

snake = Snake()
food = Food()
score = Score()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1) #to make the animation look good.
    
    snake.move_the_body() # movement function
    
    screen.listen()    #move according to key presses
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    # screen.onkey(snake_escape, "Escape")

    # eating the food and regrowing the food
    if snake.head.distance(food)<15:
        food.move_food()
        snake.extend_snake()
        score.increase_score()

        
    # detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.game_over()
        game_is_on = False
        
    # # detect collision with tail
    # for block in snake.chain:
    #     if block == snake.head:
    #         pass
    #     elif snake.head.distance(block) < 15:
    #         score.game_over()
    #         game_is_on = False
            
screen.exitonclick()
print("Game ended")
print(f"Your final score is: {score.score}")

# todo: Add high score
# todo: Add hurdles and mazes
# todo: Add special red food that lasts 10 seconds, and adds blocks depending on how early you eat it.
# todo: Add levels
# todo: Add sound!? (idk) it will be good to experience and show on paper but idk how to do that.
