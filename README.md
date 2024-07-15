# 4x4 Tic-Tac-Toe Game and Solver

## Table of Contents
1. [About](#about)
2. [How to Play](#how-to-play)
3. [Class and File Descriptions](#class-and-file-descriptions)
4. [Some Design Decisions and Tradeoffs](#design-decisions-and-tradeoffs)
5. [Future Improvement](#future-improvements)

## About
This project implements a 4x4 tic-tac-toe game. The implementation is designed 
to be flexible and efficient, and it adheres to software engineering best 
practices.

## How to Play

This 4x4 Tic-Tac-Toe game offers both single-player (against AI) and multiplayer (human vs human) modes. To start the game:

1. Run the `game.py` file:

2. You'll see a main menu with the following options:
- Single Player (vs AI)
- Multiplayer (Human vs Human)
- Exit

3. Choose your preferred mode by entering the corresponding number.

4. You will then be asked whether you would like to play a single game or a tournament, with multiple rounds. If you choose to play a tournament, enter the number of rounds you would like to play.

5. For single-player mode, you'll be asked if the AI should start.

6. The game board is a 4x4 grid. Players take turns placing their symbol (X or O) on the board.

7. To make a move, enter the row (0-3) and column (0-3) when prompted.

8. Each single game or round ends when a player wins or the board is full (draw). Each tournament ends when the indicated number of rounds has ended.

9. Winning conditions for 4x4 Tic-Tac-Toe:
- Four in a row (horizontally, vertically, or diagonally)
- Four corners
- Any 2x2 square

10. After the game ends, you'll return to the main menu where you can play again or exit.

## Class and File Descriptions

### game.py

Contains the `TicTacToeGame` class, which manages the game logic, including setup, gameplay, and tournaments. It uses the `TicTacToe4x4` class for the game board.

### enums.py

Defines two enumeration classes:
- `Player`: Represents the two players (X and O)
- `GameState`: Represents the possible game states (ONGOING, DRAW, X_WINS, O_WINS)

### tic_tac_toe_abstract.py

Contains the `TicTacToeAbstract` class, an abstract base class that defines the common interface and functionality for a Tic-Tac-Toe board.

### tic_tac_toe_4x4.py

Implements the `TicTacToe4x4` class, a concrete implementation of a 4x4 Tic-Tac-Toe board, extending `TicTacToeAbstract` with specific win conditions for a 4x4 game.

### test_4x4.py

Contains unit tests for the `TicTacToe4x4` class, covering various aspects of the game including initialization, move making, win conditions, and game state management.



## Design Decisions

### Class vs. Standalone Functions

I chose to use classes for the game board and game logic. This decision provides better encapsulation, allows for easier state management, and makes the code more modular and extensible.

**Tradeoff**: While classes introduce some overhead, the benefits of organization and potential for future expansion outIigh this cost.

### Generalizability to Different Sizes

The abstract base class `TicTacToeAbstract` is designed to be generalizable to different board sizes. HoIver, the `TicTacToe4x4` class is optimized for the 4x4 board.

**Tradeoff**: This approach allows for future expansion to other board sizes while maintaining optimization for the 4x4 case. The cost is slightly increased complexity in the class hierarchy.

### Abstract Class vs. Single Generalizable Class

I chose to use an abstract base class with concrete implementations for specific board sizes. This allows for defining different rules and win conditions for various board sizes.

**Tradeoff**: This approach provides more flexibility but requires implementing new classes for each board size.

### Game State Representation

The name of the `isGameOver` method specified in the assessment description suggests a boolean return value. I added the `get_game_state` method returns a `GameState` enum rather than a boolean. This provides more meaningful information about the game's current state.

**Tradeoff**: While this is more informative, it might be redundant.

### Board Validation

The implementation includes methods to check for valid board states, both during initialization and gameplay.

**Tradeoff**: This adds some overhead but ensures the game remains in a valid state throughout play.

### Existing Board States

The implementation allows for initializing the game with an existing board state, in addition to creating a new board.

**Tradeoff**: This adds complexity to the initialization process but provides flexibility for solving partial games or analyzing specific board states.

### Move Validation

The `is_valid_move` method checks for empty spaces rather than checking if it's still possible for a player to win.

**Tradeoff**: This simplifies the logic at the cost of potentially allowing moves in games that are effectively over.

### Winner Checking

The implementation includes both a `check_winner` method to check the overall board state and an `is_winning_move` method to check if a specific move results in a win.

**Tradeoff**: This dual approach provides flexibility but requires maintaining two separate methods. It is more efficient to check a certain move, but this also complicates the code and arguably adds some redundancy.

### Player Move Counts

Player move counts are stored in the game board class rather than in separate player classes.

**Tradeoff**: This simplifies the overall structure but couples the move count information more tightly to the board.

## Future Improvements

1. Implement more sophisticated AI strategies.
2. Add support for different board sizes.
3. Implement a graphical user interface.
4. Add network play functionality for remote multiplayer games.
5. Further refactor the code to improve modularity and reduce redundancy, particularly in the win-checking logic.
6. Add the ability to save and load game states.
7. Add additional tests
8. Add to this README!

