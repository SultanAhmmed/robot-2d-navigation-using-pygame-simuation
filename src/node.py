from utils import *

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * GRID_SIZE + GRID_SIZE // 2
        self.y = row * GRID_SIZE + GRID_SIZE // 2
        self.g_cost = float('inf')
        self.h_cost = 0.0
        self.f_cost = float('inf')
        self.parent = None
        self.is_obstacle = False

    def __lt__(self, other):
        return self.f_cost < other.f_cost

