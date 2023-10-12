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
        self.auto_pilot = False
        self.final_path  = []
        self.visited = []


    def draw(
        self,
    ):

        # draw the visited segments
        for segment in self.visited:
            pygame.draw.rect(
                self.screen,
                (66, 135, 245), # blue
                (segment["x"], segment["y"], self.block_size, self.block_size),
            )

        # draw the final path
        for segment in self.final_path:
            pygame.draw.rect(
                self.screen,
                (252, 186, 3), # yellow
                (segment["x"], segment["y"], self.block_size, self.block_size),
                2
            )
            
        # draw the snake segments
        for segment in self.segments:
            # draw  a rectangle
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                (segment["x"], segment["y"], self.block_size, self.block_size),
            )

    def update(self, food):
        """Update the snake position"""

        # update the body of the snake
        for i in range(len(self.segments) - 1):
            self.segments[i]["x"] = self.segments[i + 1]["x"]
            self.segments[i]["y"] = self.segments[i + 1]["y"]

        def find_neighbors(a_segment):
            neigbors = []
            if(a_segment["x"] < 760 ):
                neigbors.append({"x": a_segment["x"] + self.block_size, "y": a_segment["y"]})
            if(a_segment["x"] > 0 ):
                neigbors.append({"x": a_segment["x"] - self.block_size, "y": a_segment["y"]})
            if(a_segment["y"] < 760 ):
                neigbors.append({"x": a_segment["x"], "y": a_segment["y"] + self.block_size})
            if(a_segment["y"] > 0 ):
                neigbors.append({"x": a_segment["x"], "y": a_segment["y"] - self.block_size})
            return neigbors
        
        def find_valid_neighbors(neighbors):
            valid_neighbors = []
            for neighbor in neighbors:
                if neighbor not in self.segments:
                    valid_neighbors.append(neighbor)
            return valid_neighbors
            
        def find_path():
            # implement BFS path finding algorithm
            visited = [] # set
            queue = [] # queue

            path_to_the_head = [self.segments[-1]]
            queue.append((self.segments[-1], path_to_the_head))

            while queue:
                a_segment, path = queue.pop(0)
                if a_segment == food.get_position():
                    self.final_path  = path
                    self.visited = visited
                    return path 
    
                neighbors = find_neighbors(a_segment)
                valid_neighbors = find_valid_neighbors(neighbors)

                for neighbor in valid_neighbors:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append((neighbor, path + [neighbor]))
            return None
                        

        if self.auto_pilot == True:
            path = find_path() # path contains all the segments of the food
            # following the path
            if (path[1]["x"] > path[0]["x"]):
                self.direction = Direction.RIGHT
            elif (path[1]["x"] < path[0]["x"]):
                self.direction = Direction.LEFT
            elif (path[1]["y"] > path[0]["y"]):
                self.direction = Direction.DOWN
            elif (path[1]["y"] < path[0]["y"]):
                self.direction = Direction.UP


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
