import pygame

from direction import Direction


class Snake:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.direction = Direction.RIGHT
        self.block_size = 40

    def draw(
        self,
    ):
        # draw  a rectangle
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.block_size, self.block_size))
        # Update the display
        pygame.display.flip()

    def update(self):
        """Update the snake position"""
        if self.direction == Direction.RIGHT:
            self.x += self.block_size
        elif self.direction == Direction.LEFT:
            self.x -= self.block_size
        elif self.direction == Direction.UP:
            self.y -= self.block_size
        elif self.direction == Direction.DOWN:
            self.y += self.block_size
