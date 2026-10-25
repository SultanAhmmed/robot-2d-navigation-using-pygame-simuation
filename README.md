# Robot 2D Navigation Simulation

A real-time 2D mobile robot navigation and pathfinding simulation built with Python and Pygame, utilizing the **A* (A-Star) search algorithm** with 8-directional movement.

---

## Features

- **A* Pathfinding Algorithm:** Computes the shortest, collision-free path from start to goal.
- **8-Directional Movement:** Evaluates orthogonal and diagonal neighbors with corner-cutting prevention.
- **Interactive Grid Controls:** Easily place obstacles, reposition the start node, and set target destinations.
- **Real-time Obstacle Collision Checks:** Validates neighboring cells before calculating movement paths.

---

## output
<img src="output.png">

---

## Controls

| Action | Control |
| :--- | :--- |
| **Draw Obstacles** | Left-Click & Drag |
| **Set Start Position** | Right-Click |
| **Set Goal Position** | Middle Mouse Click or press **`G`** |
| **Run Simulation** | **`SPACEBAR`** |
| **Clear Grid** | **`C`** |

---

## Color Legend

- 🟩 **Green:** Starting Point
- 🟥 **Red:** Goal Destination
- 🟨 **Yellow:** Calculated Path
- ⬛ **Black:** Obstacle / Wall
- ⬜ **White:** Free Space

---

## Installation & Running with `uv`

This project is configured to run smoothly with `uv`.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SultanAhmmed/robot-2d-navigation-using-pygame-simuation.git
   cd robot-2d-navigation-using-pygame-simuation
   ```

2. **Run the simulation using `uv`:**
   ```bash
   uv run main.py
   ```

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
