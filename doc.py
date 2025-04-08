
"""
    # Debugging: Print the state of collision detection
    print(f"Collision allowed: {snake.allow_collision}")
    print(f"Snake head position: {snake.head.position()}")
    for i, block in enumerate(snake.chain[1:], start=1):
        print(f"Block {i} position: {block.position()}")
        if snake.head.position() == block.position():
            print(f"Collision detected with Block {i}!")
            
            """