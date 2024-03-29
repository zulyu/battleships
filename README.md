# Battleships! 🚢
## Battleship program developed in python3 for SE320 @ Chapman University.
### Your typical game of battle boats/battleships that is playable through a terminal. 
#### Setup & Rules: 
    1. 10x10 grid will have 8 ships of variable length randomly placed about
    2. You will have 50 bullets to take down the ships that are placed down
    3. You can choose a row and column such as A3 to indicate where to shoot
    4. For every shot that hits or misses it will show up in the grid
    5. A ship cannot be placed diagonally, so if a shot hits the rest of
        the ship is in one of 4 directions, left, right, up, and down
    6. If all ships are unearthed before using up all bullets, you win else, you lose

#### Key:
    1. "." = water
    2. "O" = part of ship
    3. "X" = part of ship that was hit
    4. "#" = water that was shot with bullet, a miss because it hit no ship

#### How to run:    
To run the program locate the program in your directory on your device and use the command "python3 battleship.py" (may differ depending on the version of python that you have installed)


#### List of Issues/Features to address:
1. Currently, the size of the grid and the number of boats are set statically. Increase the scalability of the game by allowing users to choose the grid size and the number of ships dynamically in order to make the game more customizable and enjoyable for players
2. If users don't want to select the grid size or number of ships, implement a few difficulty levels (easy, medium, hard) that adjust factors like the number of ships and bullets, providing players with varying levels of challenge.
3. Currently, once a play wins the terminal prints a singular line stating "Congrats you won!" Implement a "Game Over Screen" that displays the outcome of the game (win or lose) along with relevant statistics such as the number of ships sunk and accuracy percentage.
4. Introduce an opponent mode by implementing an algorithm that randomly guesses for its shots, to provide a challenge for players. Another grid would need to be implemented for the opponent.
5. Implement a "Save Game Progress" feature that enables players to save their current game state and resume it at a later time. 
