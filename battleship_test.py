import battleboat
import pytest

def test_accuracy_percentage():
    num_ships = 8
    num_ships_s = 3
    accuracy = battleboat.calculate_accuracy_percentage(num_ships, num_ships_s)
    assert accuracy == 37.5  # Expected accuracy percentage

def test_accept_valid_bullet_placement(monkeypatch):
    # Prepare user input
    user_input = iter(["A1", "B2"])  # Simulate user input for A1 and B2
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

    grid = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Test accepting valid bullet placement
    row, col = battleboat.accept_valid_bullet_placement(grid, alphabet)
    assert row == 0
    assert col == 1  # A1 maps to row 0, col 1

    # Test accepting valid bullet placement again
    row, col = battleboat.accept_valid_bullet_placement(grid, alphabet)
    assert row == 1
    assert col == 2  # B2 maps to row 1, col 2
