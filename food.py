import pygame


class Food:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def draw(
        self,
    ):
        # draw  a rectangle
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, 40, 40))

    def get_position(self):
        return {"x": self.x, "y": self.y}