import battleboat
import pytest

def test_accuracy_percentage():
    num_ships = 8
    num_ships_s = 3
    accuracy = battleboat.calculate_accuracy_percentage(num_ships, num_ships_s)
    assert accuracy == 37.5  # Expected accuracy percentage

def test_place_ship():
    grid = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]
    ship_info = (1, 1, "right", 2)  # Ship starting at (1, 1), going right, length 2
    assert battleboat.place_ship(grid, ship_info)  # Check if ship placement succeeds
    assert grid[1][1:3] == ["O", "O"]  # Check if the ship occupies the correct cells
