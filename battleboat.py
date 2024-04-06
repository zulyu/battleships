"""
Battleship game implementation.
"""

import random
import time

GRID = [[]]
GRID_SIZE = 10
NUM_OF_SHIPS = 2
BULLETS_LEFT = 50
GAME_OVER = False
NUM_OF_SHIPS_SUNK = 0
SHIP_POSITIONS = [[]]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    Validate the grid and place a ship if valid.
    """
    global GRID

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if GRID[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        SHIP_POSITIONS.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                GRID[r][c] = "O"
    return all_valid

def try_to_place_ship_on_grid(row, col, direction, length):
    """
    Try to place a ship on the grid.
    """
    global GRID_SIZE

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1
    elif direction == "right":
        if col + length >= GRID_SIZE:
            return False
        end_col = col + length
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1
    elif direction == "down":
        if row + length >= GRID_SIZE:
            return False
        end_row = row + length
    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

def create_grid():
    """
    Create the grid and place ships randomly.
    """
    global GRID, GRID_SIZE, NUM_OF_SHIPS

    random.seed(time.time())

    rows, cols = (GRID_SIZE, GRID_SIZE)

    GRID = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(".")
        GRID.append(row)

    num_of_ships_placed = 0

    SHIP_POSITIONS.clear()

    while num_of_ships_placed != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1

def print_grid():
    """
    Print the grid.
    """
    global GRID, ALPHABET

    debug_mode = False

    ALPHABET = ALPHABET[:len(GRID) + 1]

    for row in range(len(GRID)):
        print(ALPHABET[row], end=") ")
        for col in range(len(GRID[row])):
            if GRID[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(GRID[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(GRID[0])):
        print(str(i), end=" ")
    print("")

def accept_valid_bullet_placement():
    """
    Accept valid bullet placement.
    """
    global ALPHABET, GRID

    is_valid_placement = False
    row = -1
    col = -1
    while not is_valid_placement:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if not (0 < len(placement) <= 2 and placement[0] in ALPHABET and placement[1].isdigit()):
            print("Error: Please enter one row (A-J) and one column (0-9) such as A3.")
            continue
        row = ALPHABET.find(placement[0])
        col = int(placement[1])
        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            print("Error: Please enter valid row (A-J) and column (0-9).")
            continue
        if GRID[row][col] in ("#", "X"):
            print("You have already shot a bullet here, pick somewhere else.")
            continue
        if GRID[row][col] in (".", "O"):
            is_valid_placement = True
    return row, col

def check_for_ship_sunk(row, col):
    """
    Check if a ship is sunk.
    """
    global SHIP_POSITIONS, GRID

    for position in SHIP_POSITIONS:
        start_row, end_row, start_col, end_col = position
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if GRID[r][c] != "X":
                        return False
    return True

def shoot_bullet():
    """
    Shoot a bullet at a specified location.
    """
    global GRID, NUM_OF_SHIPS_SUNK, BULLETS_LEFT

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if GRID[row][col] == ".":
        print("You missed, no ship was shot.")
        GRID[row][col] = "#"
    elif GRID[row][col] == "O":
        print("You hit!", end=" ")
        GRID[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A ship was completely sunk!")
            NUM_OF_SHIPS_SUNK += 1
        else:
            print("A ship was shot.")
    BULLETS_LEFT -= 1

def check_for_game_over():
    """
    Check if the game is over.
    """
    global NUM_OF_SHIPS_SUNK, NUM_OF_SHIPS, BULLETS_LEFT, GAME_OVER

    if NUM_OF_SHIPS == NUM_OF_SHIPS_SUNK:
        print("Congrats you won!")
        GAME_OVER = True
    elif BULLETS_LEFT <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        GAME_OVER = True

def main():
    global GAME_OVER

    print("-----Welcome to Battleships-----")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    create_grid()

    while not GAME_OVER:
        print_grid()
        print("Number of ships remaining:", NUM_OF_SHIPS - NUM_OF_SHIPS_SUNK)
        print("Number of bullets left:", BULLETS_LEFT)
        shoot_bullet()
        print("----------------------------")
        print("")
        check_for_game_over()

if __name__ == '__main__':
    main()
