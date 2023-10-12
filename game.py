import pygame
from snake import Snake
from food import Food
from direction import Direction


class Game:
    def __init__(self):
        pygame.init()
        # Create a window
        self.screen = pygame.display.set_mode((800, 800))

        # Set the title of the window
        pygame.display.set_caption("Snake Game")

        # Fill the background color of the window
        self.screen.fill((255, 255, 255))  # white color

        # game objects
        self.snake = Snake(40, 40, self.screen)
        self.food = Food(200, 200, self.screen)

    def run(self):
        clock = pygame.time.Clock()
        FPS = 10
        pause = False

        # Game loop
        running = True
        while running:
            # Check for the events
            clock.tick(FPS)  # 1 frame per second
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if not pause:
                        if event.key == pygame.K_UP:
                            self.snake.direction = Direction.UP
                        elif event.key == pygame.K_DOWN:
                            self.snake.direction = Direction.DOWN
                        elif event.key == pygame.K_LEFT:
                            self.snake.direction = Direction.LEFT
                        elif event.key == pygame.K_RIGHT:
                            self.snake.direction = Direction.RIGHT
                        elif event.key == pygame.K_a:
                            self.snake.auto_pilot = True
                    else:
                        if event.key == pygame.K_SPACE:
                            pause = False
                            self.snake = Snake(40, 40, self.screen)

            try:
                if not pause:
                    self.update()
                    self.draw()
            except Exception as e:
                pause = True
                self.game_over()  # to display the text "Game Over"

    def update(self):
        self.snake.update(self.food)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.snake.draw()
        self.food.draw()
        # update the display
        pygame.display.flip()

    def game_over(self):
        # fill
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont("Arial", 48)
        text = font.render("Game Over. Hit Space to restart!", True, (0, 0, 0))
        self.screen.blit(
            text, (400 - text.get_width() / 2, 400 - text.get_height() / 2)
        )
        pygame.display.flip()
