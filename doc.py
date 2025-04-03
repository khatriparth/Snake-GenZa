# from turtle import *
# color('magenta', 'cyan')
# speed("fastest")
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# hideturtle()
# done()

"""
                Alternate logic if this doesn't work, followed by deubgging code (courtesy of GPT-4o):
# Detect collision with itself      
    if snake.allow_collision:
        for block in snake.chain[1:]:
            # Use a small tolerance to check for collisions
            if abs(snake.head.xcor() - block.xcor()) < 1 and abs(snake.head.ycor() - block.ycor()) < 1:
                score.game_over()
                game_is_on = False

                

    # Debugging: Print the state of collision detection
    print(f"Collision allowed: {snake.allow_collision}")
    print(f"Snake head position: {snake.head.position()}")
    for i, block in enumerate(snake.chain[1:], start=1):
        print(f"Block {i} position: {block.position()}")
        if snake.head.position() == block.position():
            print(f"Collision detected with Block {i}!")
            
            """