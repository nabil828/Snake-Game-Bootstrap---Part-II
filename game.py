import pygame
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        pygame.init()
        # Create a window
        self.screen = pygame.display.set_mode((800, 600))

        # Set the title of the window
        pygame.display.set_caption("Snake Game")

        # Fill the background color of the window
        self.screen.fill((255, 255, 255))  # white color

        # game objects
        self.snake = Snake(100, 100, self.screen)
        self.food = Food(200, 200, self.screen)

    def run(self):
        # Game loop
        running = True
        while running:
            # Check for the events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw the snake
            self.snake.draw()
            self.food.draw()
