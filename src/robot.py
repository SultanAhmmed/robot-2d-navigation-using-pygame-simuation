import pygame
import math
from utils import *

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.theta = 0.0
        self.radius = 8
        self.speed = 100.0  # pixels per second

    def follow_path(self, path, dt):
        if not path:
            return False

        # Target waypoint
        target_x, target_y = path[0]
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.hypot(dx, dy)

        # If close to current waypoint, pop it and move to next
        if distance < 5:
            path.pop(0)
            return len(path) == 0

        # Face towards waypoint and move
        self.theta = math.atan2(dy, dx)
        self.x += self.speed * math.cos(self.theta) * dt
        self.y += self.speed * math.sin(self.theta) * dt
        return False

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.x), int(self.y)), self.radius)
        end_x = self.x + (self.radius + 6) * math.cos(self.theta)
        end_y = self.y + (self.radius + 6) * math.sin(self.theta)
        pygame.draw.line(surface, BLACK, (self.x, self.y), (end_x, end_y), 2)
