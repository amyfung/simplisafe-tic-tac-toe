"""
enums.py

This module defines the enumerations used in the tic-tac-toe game: Player and 
GameState. It allows for the avoidance of hard-coded symbols within the 
TicTacToeAbstract and TicTacToe4x4 classes.
"""

from enum import Enum

class Player(Enum):
    """
    Enumeration representing the players in the game.

    This enum is used to keep track of which player's turn it is,
    as well as to mark the board spaces with the appropriate player symbol.

    Attributes:
        X (str): Represents the 'X' player.
        O (str): Represents the 'O' player.
    """
    X = 'X'
    O = 'O'

class GameState(Enum):
    """
    Enumeration representing the possible states of the game.

    This enum is used to track the current state of the game,
    whether it's ongoing, ended in a draw, or won by either player.

    Attributes:
        ONGOING (str): Represents a game that is still in progress.
        DRAW (str): Represents a game that has ended in a draw.
        X_WINS (str): Represents a game won by Player X.
        O_WINS (str): Represents a game won by Player O.
    """
    ONGOING = 'Ongoing'
    DRAW = 'Draw'
    X_WINS = 'Player X wins'
    O_WINS = 'Player O wins'