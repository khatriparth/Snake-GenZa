from turtle import Screen
from snake import Snake, HEAD_COLOR, DIRECTION
from food import Food
from score import Score
import time


screen = Screen()

screen.tracer(0)
screen.title("Snake GenZa")
screen.bgcolor("black")
screen.setup(width=600, height=600)

snake = Snake()
snake.head.color(HEAD_COLOR)
snake.head.setheading(DIRECTION)
food = Food()
score = Score()
player_name = screen.textinput("High Score", "Enter your name: ")

game_is_on = True
screen.listen()
screen.ontimer(snake.enable_collision, 1000) # enable collision after 1 second

def snake_escape():
    if not game_is_on:
        screen.bye()
        
def start_game():
    global game_is_on
    game_is_on = True
    
    while game_is_on:
        screen.update()
        time.sleep(0.1) #to make the animation look good.
        
        snake.move_the_body() # movement function
        
    #change directions according to key presses
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")
        screen.onkey(snake_escape, "Escape")
    
        # eating the food and regrowing the food
        if snake.head.distance(food)<15:
            food.move_food()
            snake.extend_snake()
            score.increase_score()
    
            
    # Detect collision with the walls
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            score.game_over()
            game_is_on = False
            
    # Detect collision with itself
        if snake.allow_collision:
            for block in snake.chain[1:]:
                # Use a small tolerance to check for collisions
                if abs(snake.head.xcor() - block.xcor()) < 1 and abs(snake.head.ycor() - block.ycor()) < 1:
                    """
                     if absolute values of BOTH x and y coordinates of head and block are less than 1
                       (reiterated for each block in the chain)
                       Tried position == position but it didn't work
                       tried distance() before that but it didn't work either
                    """
                    score.game_over()
                    game_is_on = False

start_game()

screen.onkey(start_game, "Escape")


    
        
screen.exitonclick()
print(f"Your final score is: {score.score}")
score.update_high_scores(player_name, score.score)

# todo: reset the game by a key input when game over ## Done
# todo: move the snake in a random direction every time the game starts. ## Done
# todo: Add high score keeping mechanism. ## Done
# todo: Add high score showing mechanism.
# todo: Add an option to restart the game from the 'game over' screen.
# todo: Add an option to pause the game.
# todo: Add hurdles and mazes.
# todo: Add special red food that lasts 10 seconds, and adds blocks depending on how early you eat it.
# todo: Add lives
# todo: Add levels
# todo: Add sound!? (idk) it will be good to experience and show on paper but idk how to do that.
# todo: Add a scoreboard on the left side top of screen: Dynamically tells the next high score to beat.