# NEOTicTacToe

Neo Tic-Tac-Toe is a Python-based implementation of the classic Tic-Tac-Toe, evolved through three distinct stages of development featuring both Player vs Player and Player vs AI modes. It transitions from a command-line interface logic engine to a fully interactive graphical application powered by Pygame.

## Features

- **Retro UI:** Neon color palette, dynamic background animations, and screen shake effects.
- **Unbeatable AI:** Challenge the Hard mode powered by the Minimax algorithm, or practice against the Easy Random AI.
- **Dual Interface:** Choose between the full GUI experience (Pygame) or the fast CLI version using `pygame_main.py` or `main.py`.
- **Immersive Audio:** Custom sound effects for moves, wins, and interactions.
- **Flexible Gameplay:** Supports Human vs. Human and Human vs. AI modes.

## Project Structure

- `src/AI`: Contains AI logic (Random AI and Minimax AI).
- `src/UI`: Handles the user interface, including the retro effects factory and menus.
- `src/controllers`: Manages game logic and state flow.
- `src/model`: Core game data structures (Board, Game Rules).
- `src/Sounds`: Sound resource management.

## Prerequisites

- Python 3.x
- [Pygame](https://www.pygame.org/)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rmit-nct/NEOTicTacToe.git
    cd NEOTicTacToe
    ```

2.  **Install dependencies:**
    ```bash
    pip install pygame
    ```

## How to Play

### Graphical Version (Pygame)
Experience the full retro theme with visual effects and sound.

1.  **Run the game:**
    ```bash
    python pygame_main.py
    ```
2.  **Controls:**
    - **Menu:** Click on the buttons to select your opponent (PvP, AI Easy, or AI Hard).
    - **Gameplay:** Use your **Mouse** to click on the grid cells to place your mark.
    - **Post-Game:** Choose to Restart, return to Menu, or Quit via the on-screen buttons.

### Console Version
A lightweight text-based version for quick play in the terminal.

1.  **Run the game:**
    ```bash
    python main.py
    ```
2.  **Controls:**
    - **Menu:** Enter `1`, `2`, or `3` to select the game mode.
    - **Gameplay:** Enter a number from **1-9** to place your mark on the corresponding cell.
      ```
       1 | 2 | 3
      -----------
       4 | 5 | 6
      -----------
       7 | 8 | 9
      ```
    - **Post-Game:** Follow the prompts to play again or exit.
