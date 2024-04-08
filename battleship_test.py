import battleboat
import pytest

def test_accuracy_percentage():
    num_ships = 8
    num_ships_s = 3
    accuracy = battleboat.calculate_accuracy_percentage(num_ships, num_ships_s)
    assert accuracy == 37.5  # Expected accuracy percentage
