"""
    -------BATTLESHIPS-------
    1. A 10x10 grid will have 8 ships of variable length randomly placed about
    2. You will have 50 bullets to take down the ships that are placed down
    3. You can choose a row and column such as A3 to indicate where to shoot
    4. For every shot that hits or misses it will show up in the grid
    5. A ship cannot be placed diagonally, so if a shot hits the rest of
        the ship is in one of 4 directions, left, right, up, and down
    6. If all ships are unearthed before using up all bullets, you win else, you lose

    Legend:
    1. "." = water
    2. "O" = part of ship
    3. "X" = part of ship that was hit
    4. "#" = water that was shot with bullet, a miss because it hit no ship
"""

import random
import time

# * * * GLOBAL VARIABLES * * *
GRID = [[]]
GRID_SIZE = 10 # grid size
NUM_OF_SHIPS = 2 # number of ships to place
BULLETS_LEFT = 50 # number of bullets left
GAME_OVER = False # game status
NUM_OF_SHIPS_SUNK = 0 # number of ships sunk
SHIP_POSITIONS = [[]] # ship positions
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alphabet letters

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
# will check the row/column to see if a ship can be placed
# * * *
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

def try_to_place_ship_on_grid(row, col, direction, length):
#  based on direction will call helper method to try and place a ship on the grid
# * * *
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
# will create a 10x10 grid & randomly place down ships of different sizes in different directions
# * * *
    global grid
    global GRID_SIZE
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (GRID_SIZE, GRID_SIZE)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1


def print_grid():
# will print the grid with rows A-J and columns 0-9
# * * *
    global grid
    global ALPHABET

    debug_mode = False #change to true to see the location of the boats

    ALPHABET = ALPHABET[0: len(grid) + 1]

    for row in range(len(grid)):
        print(ALPHABET[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def accept_valid_bullet_placement():
# will get valid row & column to place bullet location
# * * *
    global ALPHABET
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        row = ALPHABET.find(row)
        if not -1 < row < GRID_SIZE:
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not -1 < col < GRID_SIZE:
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True

    return row, col


def check_for_ship_sunk(row, col):
# if all parts of a ship have been shot it is sunk (increment ships sunk var)
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # ! ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True


def shoot_bullet():
# update grid and ships based on where the bullet landed
# * * *
    global grid
    global NUM_OF_SHIPS_SUNK
    global BULLETS_LEFT

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if grid[row][col] == ".":
        print("You missed, no ship was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A ship was completely sunk!")
            NUM_OF_SHIPS_SUNK += 1
        else:
            print("A ship was shot")

    BULLETS_LEFT -= 1


def check_for_game_over():
# if all ships have been sunk/there are no more bullets then the game is over
# * * *
    global NUM_OF_SHIPS_SUNK
    global NUM_OF_SHIPS
    global BULLETS_LEFT
    global GAME_OVER

    if NUM_OF_SHIPS == NUM_OF_SHIPS_SUNK:
        print("Congrats you won!")
        GAME_OVER = True
    elif BULLETS_LEFT <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        GAME_OVER = True


def main():
    # main entry point of application that runs the game loop
    global GAME_OVER

    print("-----Welcome to Battleships-----")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    create_grid()

    while GAME_OVER is False:
        print_grid()
        print("Number of ships remaining: " + str(NUM_OF_SHIPS - NUM_OF_SHIPS_SUNK))
        print("Number of bullets left: " + str(BULLETS_LEFT))
        shoot_bullet()
        print("----------------------------")
        print("")
        check_for_game_over()


if __name__ == '__main__':
    # will only be called when the program is run from a terminal
    main()
