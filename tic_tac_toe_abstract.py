"""
tic_tac_toe_abstract.py

This module defines an abstract base class for a Tic-Tac-Toe game board.
It provides a flexible structure that can be extended to create various
Tic-Tac-Toe game variants of different sizes and winning conditions.

"""

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Set
from dataclasses import dataclass, field
from enums import Player, GameState

@dataclass
class TicTacToeAbstract(ABC):
    """
    An abstract base class representing a Tic-Tac-Toe game board.

    This class provides a common interface and shared functionality for
    different variants of Tic-Tac-Toe games. It handles board initialization,
    move validation, and basic game state tracking.

    Attributes:
        size (int): The size of the game board (e.g., 3 for a 3x3 board).
        initial_state (Optional[List[List[str]]]): The initial state of the board.
        current_player (Player): The player whose turn it is.
        _board (List[List[str]]): The current state of the game board.
        _empty_cells (Set[Tuple[int, int]]): Set of empty cell coordinates.
        _x_count (int): The number of X symbols on the board.
        _o_count (int): The number of O symbols on the board.
        _winner (Optional[Player]): The winner of the game, if any.

    Abstract Methods:
        is_winning_move(row: int, col: int) -> bool
        check_winner() -> Optional[Player]
    """
    size: int
    initial_state: Optional[List[List[str]]] = None
    current_player: Optional[Player] = Player.X
    _board: List[List[str]] = field(init=False)
    _empty_cells: Set[Tuple[int, int]] = field(init=False)
    _x_count: int = field(init=False, default=0)
    _o_count: int = field(init=False, default=0)
    _winner: Optional[Player] = field(init=False, default=None)

    # ==========================================================================
    # Initializing the board
    # ==========================================================================
    def __post_init__(self):
        """
        Initialize the game board after the object is created.

        This method is automatically called after the object is instantiated.
        It sets up the game board based on the provided initial state or
        creates a new empty board if no initial state is provided.

        Raises:
            ValueError: If the board size is less than 3x3.
        """
        if self.size < 3:
            raise ValueError("Board size must be at least 3x3")
        
        if self.initial_state:
            self._initialize_from_state()
        else:
            self._initialize_new_board()

    def _initialize_new_board(self) -> None:
        """
        Initialize a new empty game board.

        This method creates an empty board of the specified size and
        initializes the set of empty cells.
        """
        # Create an empty board
        self._board = [["" for _ in range(self.size)] for _ in range(self.size)]
        # Initialize the set of empty cells with all board positions
        self._empty_cells = {(r, c) for r in range(self.size) for c in range(self.size)}

    def _initialize_from_state(self) -> None:
        """
        Initialize the game board from a given initial state.

        This method sets up the board based on the provided initial state,
        validates the state, and initializes game counters and the current player.

        Raises:
            ValueError: If the initial board state is invalid.
        """
        if not self._is_valid_board():
            raise ValueError("Invalid initial board state")

        self._board = self.initial_state
        # Identify empty cells from the initial state
        self._empty_cells = {(r, c) for r in range(self.size) for c in range(self.size) if not self._board[r][c]}
        self._x_count, self._o_count = self._count_moves()
        
        # Determine the current player if not specified
        if not self.current_player:
            self.current_player = Player.X if self._x_count <= self._o_count else Player.O
        elif (self.current_player == Player.X and self._x_count > self._o_count) or \
             (self.current_player == Player.O and self._o_count > self._x_count):
            raise ValueError("Provided current player is inconsistent with the board state")

        self._winner = self.check_winner()

    def _is_valid_board(self) -> bool:
        """
        Check if the initial board state is valid.

        Returns:
            bool: True if the board state is valid, False otherwis\e.
        """
        # Check board dimensions
        if len(self.initial_state) != self.size or any(len(row) != self.size for row in self.initial_state):
            return False

        # Count moves and check for validity
        x_count, o_count = self._count_moves()
        return x_count and abs(x_count - o_count) <= 1

    def _count_moves(self) -> Tuple[Optional[int], Optional[int]]:
        """
        Count the number of moves made by each player.

        Returns:
            Tuple[Optional[int], Optional[int]]: A tuple containing the count of X and O moves.
                Returns (None, None) if an invalid symbol is found on the board.
        """
        x_count = o_count = 0
        for row in self._board:
            for cell in row:
                if cell == Player.X.value:
                    x_count += 1
                elif cell == Player.O.value:
                    o_count += 1
                elif cell:  # If cell contains an invalid symbol
                    return None, None

        return x_count, o_count

    def reset(self) -> None:
        """
        Reset the game board to have all empty cells.

        This method clears the board, resets all counters, and sets the current 
        player to X.
        """
        self._initialize_new_board()
        self.current_player = Player.X
        self._winner = None
        self._x_count = self._o_count = 0

    # ==========================================================================
    # Making moves
    # ==========================================================================
    def make_move(self, row: int, col: int) -> bool:
        """
        Attempt to place the current player's symbol on the board.

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.

        Returns:
            bool: True if the move was valid and made, False otherwise.
        """
        

    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Check if a move is valid (i.e., the cell is empty).

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        

    # ==========================================================================
    # Solver methods that check the game state
    # ==========================================================================
    
    def is_game_over(self) -> bool:
        """
        Check whether the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        

    def get_game_state(self) -> GameState:
        """
        Get the current game state.

        Returns:
            GameState: The current state of the game.
        """
        

    def any_moves_left(self) -> bool:
        """
        Check whether there are any moves left.

        Args:
            board (AbstractBoard): The game board.

        Returns:
            bool: True if there are moves left, False otherwise.
        """
        return (self._o_count + self._x_count) < self._size ** 2
    
    # ==========================================================================
    # Checking winning
    # ==========================================================================
    @abstractmethod
    def is_winning_move(self, row: int, col: int):
        """
        Check whether the last move resulted in a win.

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.

        Returns:
            bool: True if the move resulted in a win or False otherwise.
        """
        

    @abstractmethod
    def check_winner(self) -> Optional[Player]:
        """
        Checks whether there is a winner of the tic-tac-toe game based on the
        horizontal, vertical, and diagonal win conditions. Returns the winner,
        if any, or None.
        
        Returns:
            Optional[str]: The winner ('X' or 'O') or None if there is no winner.
        """
    
    # ==========================================================================
    # Properties
    # ==========================================================================

    @property
    def valid_moves(self) -> List[Tuple[int, int]]:
        return list(self._empty_cells)
    
    @property
    def game_state(self) -> GameState:
        """
        Get the current state of the game.

        Returns:
            GameState: The current state of the game (X_WINS, O_WINS, DRAW, or ONGOING).
        """
        if self._winner == Player.X:
            return GameState.X_WINS
        elif self._winner == Player.O:
            return GameState.O_WINS
        elif not self._empty_cells:
            return GameState.DRAW
        return GameState.ONGOING

    @property
    def valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of all valid moves (empty cells) on the board.

        Returns:
            List[Tuple[int, int]]: A list of (row, col) tuples representing valid moves.
        """
        return list(self._empty_cells)


    def __str__(self) -> str:
        """
        Get a string representation of the current board state.

        Returns:
            str: A string representation of the board.
        """
        return "\n".join("|" + "|".join(cell if cell else "_" for cell in row) + "|" for row in self._board)

    def print_board(self) -> None:
        """
        Print the current board state to the console.
        """
        print(f"\n{self}\n")