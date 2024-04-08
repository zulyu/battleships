import battleboat
import pytest

def test_accuracy_percentage():
    num_ships = 8
    num_ships_s = 3
    accuracy = battleboat.calculate_accuracy_percentage(num_ships, num_ships_s)
    assert accuracy == 37.5  # Expected accuracy percentage

def test_check_for_ship_sunk():
    # Test case 1: Ship not sunk
    grid1 = [
        ["O", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]
    assert not battleboat.check_for_ship_sunk(0, 0, grid1)

    # Test case 2: Ship sunk
    grid2 = [
        ["X", "X", "X"],
        [".", ".", "."],
        [".", ".", "."]
    ]
    assert battleboat.check_for_ship_sunk(0, 0, grid2)

    # Test case 3: No ship at the specified position
    grid3 = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]
    assert not battleboat.check_for_ship_sunk(0, 0, grid3)

    # Test case 4: Ship partially hit
    grid4 = [
        ["O", "X", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]
    assert not battleboat.check_for_ship_sunk(0, 0, grid4)
