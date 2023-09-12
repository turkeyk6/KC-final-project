import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position and velocity
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_velocity = (1, 0)

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game loop variables
running = True
clock = pygame.time.Clock()

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_velocity != (0, 1):
                snake_velocity = (0, -1)
            elif event.key == pygame.K_DOWN and snake_velocity != (0, -1):
                snake_velocity = (0, 1)
            elif event.key == pygame.K_LEFT and snake_velocity != (1, 0):
                snake_velocity = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_velocity != (-1, 0):
                snake_velocity = (1, 0)

    # Update snake position
    new_head = (snake[0][0] + snake_velocity[0], snake[0][1] + snake_velocity[1])
    snake.insert(0, new_head)

    # Check if snake ate the food
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check for collision with walls or itself
    if (
        snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or
        snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT or
        snake[0] in snake[1:]
    ):
        running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw food
    pygame.draw.rect(screen, GREEN, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()

    # Control game speed
    clock.tick(10)

# Quit Pygame
pygame.quit()
