import pygame
import random

class Environment:
    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.cols = width // grid_size
        self.rows = height // grid_size
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.generate_obstacles()

    def generate_obstacles(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < 0.2:
                    self.grid[i][j] = 1

    def get_start_goal(self):
        return (0, 0), (self.rows - 1, self.cols - 1)

    def draw(self, screen, path):
        for i in range(self.rows):
            for j in range(self.cols):
                color = (255, 255, 255)
                if self.grid[i][j] == 1:
                    color = (0, 0, 0)
                pygame.draw.rect(screen, color,
                                 (j * self.grid_size, i * self.grid_size,
                                  self.grid_size, self.grid_size))
        # Draw path
        for node in path:
            pygame.draw.rect(screen, (0, 255, 0),
                             (node[1] * self.grid_size, node[0] * self.grid_size,
                              self.grid_size, self.grid_size))