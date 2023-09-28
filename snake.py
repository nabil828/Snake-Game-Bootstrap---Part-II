import pygame


class Snake:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self, ):
        # draw  a rectangle
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 40, 40))
        # Update the display
        pygame.display.flip()

