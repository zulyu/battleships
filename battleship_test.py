import battleboat
import pytest

def test_accuracy_percentage():
    num_ships = 8
    num_ships_s = 3
    accuracy = battleboat.calculate_accuracy_percentage(num_ships, num_ships_s)
    assert accuracy == 37.5  # Expected accuracy percentage

def test_create_grid():
    grid_size = 5
    num_of_ships = 2

    grid = battleboat.create_grid(grid_size, num_of_ships)

    # Check if the grid has the correct dimensions
    assert len(grid) == grid_size
    for row in grid:
        assert len(row) == grid_size

    # Check if the number of ships in the grid matches num_of_ships
    num_ships_in_grid = sum(row.count("O") for row in grid)
    assert num_ships_in_grid == num_of_ships
