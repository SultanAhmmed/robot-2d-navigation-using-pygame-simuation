# Contributing to Robot 2D Navigation Simulation

Thank you for considering contributing to this project! We welcome contributions, feature requests, bug reports, and improvements from the community.

Please take a moment to review the guidelines below before getting started.

---

## 📜 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [How Can I Contribute?](#-how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Workflow](#-development-workflow)
- [Coding Standards](#-coding-standards)

---

## 📜 Code of Conduct

Please help us maintain a friendly, welcoming, and safe environment for everybody. Be respectful and constructive in all discussions and code reviews.

---

## 🤝 How Can I Contribute?

### Reporting Bugs

If you find a bug or unexpected behavior:

1. **Check existing issues** to make sure it hasn't already been reported.
2. If not found, **open a new issue** with the following details:
   - Clear and descriptive title.
   - Steps to reproduce the bug.
   - Expected behavior vs. actual behavior.
   - Environment details (Python version, Pygame version, OS).

### Suggesting Enhancements

Ideas for improvements (e.g., dynamic path planning, new UI elements, continuous kinematic movement) are welcome! To suggest an enhancement:

1. Open an issue with the label `enhancement`.
2. Provide a detailed explanation of the proposed feature and why it would be beneficial.

### Pull Requests

1. **Fork** the repository and create your branch from `main`.
2. Ensure your code follows the project's formatting and style guidelines.
3. Keep your commits clean and write descriptive commit messages.
4. Open a **Pull Request (PR)** against the `main` branch with a summary of changes.

---

## 🛠️ Development Workflow

This project uses [`uv`](https://github.com/astral-sh/uv) for fast, reliable Python package and environment management.

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/robot-2d-navigation-using-pygame-simuation.git
   cd robot-2d-navigation-using-pygame-simuation
   ```

2. **Set up the virtual environment with `uv`:**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   uv add pygame
   ```

4. **Create a new feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

5. **Run the simulation locally to test:**
   ```bash
   uv run main.py
   ```

---

## 🎨 Coding Standards

To maintain clean and readable code across the project, please follow these guidelines:

- **PEP 8 Compliance:** Adhere to standard Python styling guidelines (4-space indentation, clear variable naming, proper docstrings).
- **Clear Comments:** Write clear inline comments and docstrings explaining complex mathematical logic or algorithmic steps (e.g., A* heuristics, node evaluations).
- **Single Responsibility:** Keep functions and classes focused on single tasks (e.g., grid drawing vs. path calculation).

---

Thank you for contributing! 🚀
