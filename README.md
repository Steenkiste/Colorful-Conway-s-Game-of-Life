# Colorful Conway's Game of Life

A Python implementation of Conway's Game of Life using **Python** and **Pygame**. This project adds colors to each living cell and allows you to draw on the grid when the game is paused.

## Table of Contents
- [Overview](#overview)
- [How to play it ?](#how-to-play-it)
- [Gameplay Controls](#gameplay-controls)
- [How It Works](#how-it-works)
- [Project-Structure](#project-structure)
- [Customization](#customization)
- [License](#license)
- [Credits](#credits)

## Overview
This project was made to push my understanding of programming fundamentals and the use of a graphics library like **Pygame**. I used **Python** for all the logic—managing a grid to track cell placement and **Pygame** for rendering.
<br />
<br />
The rules of Conway's Game of Life are :
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

<img src="./ccwgol.gif"/>

## How to play it ?
### On navigator
You can play it on Itch.io : https://chivalryincode.itch.io/conways-game-of-life

### On your computer
1. **Download** this repository :
   ```bash
   git clone https://github.com/Dimitri-van-Steenkiste/Colorful-Conways-Game-of-Life.git
2. Install all dependencies : Python and Pygame.
3. Run the game using python :
   ```bash
   python colorful_conway_s_game_of_life.py

## Gameplay Controls
- Left mouse : Draw on the grid by adding or remove a cell.
- Space key ! Start or pause the game.

## Project Structure
├── color.py <br />
├── colorful_conway_s_game_of_life.py <br />
└── README.md (this file)

- **colorful_colorful_conway_s_game_of_life.py**: The main script containing the game loop and logic.
- **color.py**: A file containing RGB tuples for different colors used in the game.

## Customization
- Grid Size: Adjust **GRID** in colorful_conway_s_game_of_life.py (default is 80).
- Colors: Edit **COLORS** in color.py to change available colors.
- Speed: Adjust **WAIT_TIME** in colorful_conway_s_game_of_life.py to change simulation speed (default is 80).

## License
This project is open-source. You can use, modify, and distribute it. If you include major changes or use it as part of your project, consider giving credit in your own README.

## Credit
Conway's Game of Life rules: Wikipedia
Pygame (https://www.pygame.org/)
