from game2dboard import Board
from datastructures import Graph
from algorithms import quicksort, minesNextTo

import random
import time

# Constants and globals for board setup and game state
SIZE = 10  # Board size
NUM_MINES = 15  # Total number of mines
SCOREBOARD_PATH = "scoreboard.txt"  # File path for the scoreboard
logical_board = Graph(SIZE)  # Graph data structure for game logic
visual_board = Board(SIZE, SIZE)  # 2D game board for display
start_time = time.time()  # Game start time for score calculation
mines = []  # List to store mine locations

# Function to place mines randomly on the board
def place_mines():
    global mines
    mines.clear()  # Clear previous mine locations

    # Randomly select and place mines, ensuring no duplicates
    while len(mines) < NUM_MINES:
        x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
        if (x, y) not in mines:
            mines.append((x, y))
            logical_board.get_node(x, y).value = 'mine'

# Handles mouse click events on the board
def handleClick(btn, row, col):
    node = logical_board.get_node(row, col)  # Get the node at clicked position

    # Right-click to toggle flag or cover
    if btn == 3:
        if visual_board[row][col] == 'cover':
            visual_board[row][col] = 'flag'
            node.value = 'flag'
        elif visual_board[row][col] == 'flag':
            visual_board[row][col] = 'cover'
            node.value = 'cover'
        return

    # Left-click to reveal tile or trigger game over
    if btn == 1:
        if node.value == 'cover':
            clearTiles(row, col)
            check_win_condition()
        elif node.value == 'mine':
            reveal_mines()
            print("Game Over! You hit a mine.")

# Reveals all mines on the board
def reveal_mines():
    for x in range(SIZE):
        for y in range(SIZE):
            if logical_board.get_node(x, y).value == 'mine':
                visual_board[x][y] = 'mine'

# Recursively clears tiles without adjacent mines
def clearTiles(x, y, visited=None):
    if visited is None:
        visited = set()

    # Base case checks for recursion
    if x < 0 or y < 0 or x >= SIZE or y >= SIZE:
        return
    if (x, y) in visited:
        return
    if logical_board.get_node(x, y).value != 'cover':
        return

    visited.add((x, y))
    adjacent_mines = minesNextTo(x, y, mines, SIZE)

    # Update cell based on adjacent mines
    logical_board.get_node(x, y).value = str(adjacent_mines) if adjacent_mines > 0 else 'clear'
    visual_board[x][y] = str(adjacent_mines) if adjacent_mines > 0 else None

    # Recurse for adjacent cells if no adjacent mines
    if adjacent_mines == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                clearTiles(x + dx, y + dy, visited)

# Check if the win condition is met
def check_win_condition():
    # Check all non-mine cells are uncovered
    if all(node.value != 'cover' for row in logical_board.nodes for node in row if node.value != 'mine'):
        print("Congratulations! You've cleared all mines.")
        update_scoreboard(SCOREBOARD_PATH, time.time() - start_time)

# Updates the scoreboard with new scores
def update_scoreboard(file_path, new_score):
    try:
        with open(file_path, 'r') as file:
            scores = [float(line.split(') ')[1]) for line in file if line.strip()]
    except FileNotFoundError:
        scores = []
#create a list of scores and append to it
    scores.append(round(float(new_score), 3))
    ranked_scores = quicksort(scores)
#Opening the file to write the score to it
    with open(file_path, 'w') as file:
        for i, score in enumerate(ranked_scores, start=1):
            file.write(f"{i}) {score}\n")

    print(f"Score saved to {SCOREBOARD_PATH}")

# Main function to initialize and start the game
def main():
    place_mines()  # Place mines on the board

    visual_board.cell_size = 25  # Set visual board cell size
    visual_board.on_mouse_click = handleClick  # Set up click handler
    visual_board.fill('cover')  # Fill board with covered tiles
    visual_board.show()  # Display the board

if __name__ == '__main__':
    main()  # Start the game
