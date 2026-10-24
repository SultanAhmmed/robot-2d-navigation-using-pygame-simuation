import pygame
import math
from src.utils import *
from src.astar_search import a_star_search
import sys
import time
from src.node import Node
from src.robot import Robot

pygame.init()


# Initialize grid map
grid = [[Node(r, c) for c in range(COLS)] for r in range(ROWS)]

start_node = grid[5][5]
goal_node = grid[ROWS - 6][COLS - 6]
robot = Robot(start_node.x, start_node.y)

path = []
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Navigation - Phase 2: A* Pathfinding")

while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Run A*
                # Reset cost matrices for fresh search
                for r in range(ROWS):
                    for c in range(COLS):
                        grid[r][c].g_cost = float('inf')
                        grid[r][c].f_cost = float('inf')
                        grid[r][c].parent = None
                path = a_star_search(grid, start_node, goal_node)
                if path:
                    robot.x, robot.y = path[0]  # Reset robot position to start
            elif event.key == pygame.K_c:  # Clear grid
                path = []
                for r in range(ROWS):
                    for c in range(COLS):
                        grid[r][c].is_obstacle = False

        # Mouse controls for editing environment
        if pygame.mouse.get_pressed()[0]:  # Left Click: Draw obstacles
            pos = pygame.mouse.get_pos()
            r, c = pos[1] // GRID_SIZE, pos[0] // GRID_SIZE
            if 0 <= r < ROWS and 0 <= c < COLS:
                node = grid[r][c]
                if node != start_node and node != goal_node:
                    node.is_obstacle = True

        elif pygame.mouse.get_pressed()[2]:  # Right Click: Set Start
            pos = pygame.mouse.get_pos()
            r, c = pos[1] // GRID_SIZE, pos[0] // GRID_SIZE
            if 0 <= r < ROWS and 0 <= c < COLS:
                start_node = grid[r][c]
                start_node.is_obstacle = False
                robot.x, robot.y = start_node.x, start_node.y

        elif pygame.mouse.get_pressed()[1]:  # Middle Click: Set Goal
            pos = pygame.mouse.get_pos()
            r, c = pos[1] // GRID_SIZE, pos[0] // GRID_SIZE
            if 0 <= r < ROWS and 0 <= c < COLS:
                goal_node = grid[r][c]
                goal_node.is_obstacle = False

    # Robot movement along computed path
    if path:
        reached_end = robot.follow_path(path, dt)

    # --- Rendering ---
    screen.fill(WHITE)

    # Draw grid and obstacles
    for r in range(ROWS):
        for c in range(COLS):
            node = grid[r][c]
            rect = pygame.Rect(c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if node.is_obstacle:
                pygame.draw.rect(screen, OBSTACLE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)  # Grid lines

    # Draw Path
    if len(path) > 1:
        for i in range(len(path) - 1):
            pygame.draw.line(screen, YELLOW, path[i], path[i+1], 4)

    # Draw Start and Goal nodes
    pygame.draw.circle(screen, GREEN, (start_node.x, start_node.y), GRID_SIZE // 3)
    pygame.draw.circle(screen, RED, (goal_node.x, goal_node.y), GRID_SIZE // 3)

    # Draw Robot
    robot.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
