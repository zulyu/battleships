import random
import time

def validate_grid_and_place_ship(grid, ship_positions, start_row, end_row, start_col, end_col):
    """
    Validate the grid and place a ship if valid.
    """
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

def try_to_place_ship_on_grid(grid, grid_size, ship_positions, row, col, direction, length):
    """
    Try to place a ship on the grid.
    """
    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1
    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1
    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length
    return validate_grid_and_place_ship(grid, ship_positions, start_row, end_row, start_col, end_col)

def create_grid(grid_size, num_of_ships):
    """
    Create the grid and place ships randomly.
    """
    random.seed(time.time())

    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    ship_positions = []

    while len(ship_positions) != num_of_ships:
        random_row = random.randint(0, grid_size - 1)
        random_col = random.randint(0, grid_size - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(grid, grid_size, ship_positions, random_row, random_col, direction, ship_size):
            pass

    return grid, ship_positions

def print_grid(grid):
    """
    Print the grid.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    debug_mode = False

    alphabet = alphabet[:len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
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

def accept_valid_bullet_placement(grid, alphabet):
    """
    Accept valid bullet placement.
    """
    is_valid_placement = False
    row = -1
    col = -1
    while not is_valid_placement:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if not (0 < len(placement) <= 2 and placement[0] in alphabet and placement[1].isdigit()):
            print("Error: Please enter one row (A-J) and one column (0-9) such as A3.")
            continue
        row = alphabet.find(placement[0])
        col = int(placement[1])
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            print("Error: Please enter valid row (A-J) and column (0-9).")
            continue
        if grid[row][col] in ("#", "X"):
            print("You have already shot a bullet here, pick somewhere else.")
            continue
        if grid[row][col] in (".", "O"):
            is_valid_placement = True
    return row, col

def check_for_ship_sunk(row, col, ship_positions, grid):
    """
    Check if a ship is sunk.
    """
    for position in ship_positions:
        start_row, end_row, start_col, end_col = position
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True

def shoot_bullet(grid, ship_positions, bullets_left):
    """
    Shoot a bullet at a specified location.
    """
    row, col = accept_valid_bullet_placement(grid, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("")
    print("----------------------------")

    if grid[row][col] == ".":
        print("You missed, no ship was shot.")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col, ship_positions, grid):
            print("A ship was completely sunk!")
        else:
            print("A ship was shot.")
    bullets_left -= 1

    return bullets_left

def check_for_game_over(ship_positions, num_of_ships_sunk, num_of_ships, bullets_left):
    """
    Check if the game is over.
    """
    if num_of_ships == num_of_ships_sunk:
        print("Congrats you won!")
        return True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        return True
    return False

def main():
    print("-----Welcome to Battleships-----")
    print("You have 50 bullets to take down 8 ships, may the battle begin!")

    grid_size = 10
    num_of_ships = 2
    bullets_left = 50
    num_of_ships_sunk = 0

    grid, ship_positions = create_grid(grid_size, num_of_ships)

    game_over = False
    while not game_over:
        print_grid(grid)
        print("Number of ships remaining:", num_of_ships - num_of_ships_sunk)
        print("Number of bullets left:", bullets_left)
        bullets_left = shoot_bullet(grid, ship_positions, bullets_left
