import pygame
from snake import Snake
from food import Food
from direction import Direction


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
        clock = pygame.time.Clock()
        FPS = 10

        # Game loop
        running = True
        while running:
            # Check for the events
            clock.tick(FPS)  # 1 frame per second
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.direction = Direction.UP
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT:
                        self.snake.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = Direction.RIGHT

            self.update()
            self.draw()

    def update(self):
        self.snake.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.snake.draw()
        self.food.draw()
