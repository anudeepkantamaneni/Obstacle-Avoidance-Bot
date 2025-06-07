import pygame
import sys
from environment import Environment
from ai_navigation import astar_path

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load Environment
env = Environment(WIDTH, HEIGHT, GRID_SIZE)
start, goal = env.get_start_goal()
path = astar_path(env.grid, start, goal)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    env.draw(screen, path)
    pygame.display.flip()
    clock.tick(30)