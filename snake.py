import random
import pygame

from direction import Direction


class Snake:
    def __init__(self, x, y, screen):
        # self.x = x
        # self.y = y
        self.screen = screen
        self.direction = Direction.RIGHT
        self.block_size = 40
        self.segments = [
            {"x": x, "y": y},
            {"x": x + self.block_size, "y": y},
            {"x": x + self.block_size * 2, "y": y},
            {"x": x + self.block_size * 3, "y": y},
        ]
        # the head is the last element in the list

    def draw(
        self,
    ):
        for segment in self.segments:
            # draw  a rectangle
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                (segment["x"], segment["y"], self.block_size, self.block_size),
            )
        # Update the display
        pygame.display.flip()

    def update(self, food):
        """Update the snake position"""

        # update the body of the snake
        for i in range(len(self.segments) - 1):
            self.segments[i]["x"] = self.segments[i + 1]["x"]
            self.segments[i]["y"] = self.segments[i + 1]["y"]

        # update the head of the snake
        if self.direction == Direction.RIGHT:
            self.segments[-1]["x"] += self.block_size
        elif self.direction == Direction.LEFT:
            self.segments[-1]["x"] -= self.block_size
        elif self.direction == Direction.UP:
            self.segments[-1]["y"] -= self.block_size
        elif self.direction == Direction.DOWN:
            self.segments[-1]["y"] += self.block_size

        # detect collision with food,
        if self.detect_collision_with_food(food):
            self.increase_the_size_of_snake_by_one()
            self.change_the_location_of_the_food(food)

        # detect collision with the wall
        if self.detect_collision_with_wall():
            raise "Game over - collision with the wall"
    
        # detect collision with itself
        if self.detect_collision_with_itself():
            raise "Game over - collision with itself"

    def detect_collision_with_food(self, food):
        """Detect collision with food"""
        if (self.segments[-1]["x"] == food.x) and (self.segments[-1]["y"] == food.y):
            return True

    def increase_the_size_of_snake_by_one(self):
        """Increase the size of snake by one"""
        # detect the direction of the snake
        if self.direction == Direction.RIGHT:
            self.segments.append(
                {
                    "x": self.segments[-1]["x"] + self.block_size,
                    "y": self.segments[-1]["y"],
                }
            )
        elif self.direction == Direction.LEFT:
            self.segments.append(
                {
                    "x": self.segments[-1]["x"] - self.block_size,
                    "y": self.segments[-1]["y"],
                }
            )
        elif self.direction == Direction.UP:
            self.segments.append(
                {
                    "x": self.segments[-1]["x"],
                    "y": self.segments[-1]["y"] - self.block_size,
                }
            )
        elif self.direction == Direction.DOWN:
            self.segments.append(
                {
                    "x": self.segments[-1]["x"],
                    "y": self.segments[-1]["y"] + self.block_size,
                }
            )

    def change_the_location_of_the_food(self, food):
        """
        Change the location of the food
        make sure it is not on the snake
        """
        while True:
            x = (
                random.randint(0, 19) * self.block_size
            )  # 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, ..., 760
            y = random.randint(0, 19) * self.block_size
            if {"x": x, "y": y} not in self.segments:
                break
        food.x = x
        food.y = y
    
    def detect_collision_with_wall(self):
        """Detect collision with the wall"""
        if self.segments[-1]["x"] < 0 or self.segments[-1]["x"] > 760:
            return True
        elif self.segments[-1]["y"] < 0 or self.segments[-1]["y"] > 760:
            return True

    def detect_collision_with_itself(self):
        """Detect collision with itself"""
        if self.segments[-1] in self.segments[:-1]:
            return True