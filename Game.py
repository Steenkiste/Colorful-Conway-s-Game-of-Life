import pygame
import random
import Color as cc

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRID = 80
CELL_WIDTH = SCREEN_WIDTH // GRID
CELL_HEIGHT = SCREEN_HEIGHT // GRID

# Functions

# Function to create a matrix which is the base of the grid
# Is used here a simple Python list Comprehension
def createMatrix(size) -> list:
    return [[0 for _ in range(size)] for _ in range(size)]

# Function that calculate the number of "neighbors" of all of the element of the matrix/grid
def countNeighbors(grid:list, x:int, y:int) -> int :
    neighbors = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(max(0, x-1), min(x+2, rows)):
        for j in range(max(0, y-1), min(y+2, cols)):
            if (i, j) != (x, y):
                neighbors += grid[i][j]
    
    return neighbors

# Function that create a new grid based of the number of neighbour of eatch "cells" of the matrix/grid
#We don't want to modify the current matrix/grid because it would calculate it for each cell and modify it on the fly
def nextGeneration(grid) -> list :
    rows = len(grid)
    cols = len(grid[0])
    newGrid = createMatrix(rows)
    
    for i in range(rows):
        for j in range(cols):
            neighbors = countNeighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors in [2, 3]:
                    newGrid[i][j] = 1
                else:
                    newGrid[i][j] = 0
            else:
                if neighbors == 3:
                    newGrid[i][j] = 1
    
    return newGrid

# Function that will draw each cells of the matrix/grid
def showGrid(screen, grid:list, playing:bool) -> None :
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows) :
        for col in range(cols):
            x = col * CELL_WIDTH
            y = row * CELL_HEIGHT

            if grid[row][col] == 1:
                if playing :
                    color = random.choice(cc.COLORS)
                else:
                    color = cc.BLACK
            else:
                color = cc.WHITE
            
            pygame.draw.rect(screen, color, (x, y, CELL_WIDTH, CELL_HEIGHT))

# Function used to draw on the grid when the game is paused
def drawOnGrid(grid, row, col):
    grid[row][col] = 1 - grid[row][col]

def main():
    # Initialization of Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Colorful Conway's Game of Life")
    clock = pygame.time.Clock()

    # Initialization of the grid and game stats
    gameGrid = createMatrix(GRID)
    running = True
    playing = False

    while running:
        screen.fill(cc.DARK_BROWN)
        
        # Initialization of inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not playing:
                mouse_x, mouse_y = event.pos
                grid_row, grid_col = mouse_y // CELL_HEIGHT, mouse_x // CELL_WIDTH
                drawOnGrid(gameGrid, grid_row, grid_col)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

        if playing:
            gameGrid = nextGeneration(gameGrid)
            pygame.time.wait(80)

        showGrid(screen, gameGrid, playing)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()