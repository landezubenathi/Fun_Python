import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SkylaH... Snake Game🐍")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Snake starting position
x, y = width / 2, height / 2

# Snake movement direction
x_change, y_change = 0, 0

# Snake body
snake_list = []
snake_length = 1

# Food properties
food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0

    # Update snake position
    x += x_change
    y += y_change

    # Boundary check
    if x >= width or x < 0 or y >= height or y < 0:
        running = False

    # Fill the screen
    screen.fill(black)

    # Draw food
    pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

    # Update snake body
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for snake collision with itself
    for segment in snake_list[:-1]:
        if segment == snake_head:
            running = False

    # Draw snake
    for segment in snake_list:
        pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])

    # Check for snake eating food
    if x == food_x and y == food_y:
        food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake_length += 1

    # Update the display
    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(snake_speed)

# Quit Pygame
pygame.quit()