import math
import heapq
from utils import *


def heuristic(node1, node2):
    # Euclidean distance heuristic
    return math.hypot(node1.row - node2.row, node1.col - node2.col)

def a_star_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    start.g_cost = 0
    start.f_cost = heuristic(start, goal)

    open_set_hash = {start}

    while open_set:
        current = heapq.heappop(open_set)[1]
        open_set_hash.remove(current)

        if current == goal:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1] # Return reversed path from start to goal

        neighbors = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for dr, dc in neighbors:
            r, c = current.row + dr, current.col + dc
            if 0 <= r < ROWS and 0 <= c < COLS:
                neighbor = grid[r][c]
                if neighbor.is_obstacle:
                    continue

                move_cost = math.hypot(dr, dc)
                temp_g_cost = current.g_cost + move_cost

                if temp_g_cost < neighbor.g_cost:
                    neighbor.parent = current
                    neighbor.g_cost = temp_g_cost
                    neighbor.h_cost = heuristic(neighbor, goal)
                    neighbor.f_cost = neighbor.g_cost + neighbor.h_cost

                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (neighbor.f_cost, neighbor))
                        open_set_hash.add(neighbor)

    return None


