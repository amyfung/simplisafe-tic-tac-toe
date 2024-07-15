from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from enums import Player, GameState


class TicTacToeAbstract(ABC):
    """Abstract class representing the common interface for a tic-tac-toe board."""

    # ==========================================================================
    # Initializing the board
    # ==========================================================================
    def __init__(
        self,
        size: int,
        initial_state: Optional[List[List[str]]] = None,
        current_player: Optional[Player] = None,
    ):
        """
        Initialize a new game board.

        This method sets up either a new empty board or initializes the board with a given state.

        Args:
            size (int): The size of the board (e.g., 3 for a 3x3 board, 4 for a 4x4 board).
            initial_state (Optional[List[List[str]]]): A 2D list representing an existing board state.
                If provided, the board will be initialized with this state. Default is None.
            current_player (Optional[Player]): The player whose turn it is.
                If not provided, it defaults to Player.X for a new board, or is determined
                based on the move count for an existing board state.

        Raises:
            ValueError: If the provided size is less than 3, or if the initial_state is invalid.

        Note:
            If initial_state is provided, the method calls _initialize_from_state to set up the board.
        """

    def _initialize_from_state(
        self, initial_state: List[List[str]], current_player: Optional[Player]
    ) -> None:
        """
        Initialize the board from a given state.

        This method is called by __init__ when an initial_state is provided. It sets up
        the board based on the given state and determines the current player.

        Args:
            initial_state (List[List[str]]): A 2D list representing the board state to initialize from.
            current_player (Optional[Player]): The player whose turn it is. If not provided,
                it's determined based on the number of moves made by each player.

        Raises:
            ValueError: If the initial_state is invalid, or if the provided current_player
                is inconsistent with the board state.

        """

    def _is_valid_board(self, board: List[List[str]]) -> bool:
        """
        Check whether the given board is valid.

        A board is considered valid if:
        1. It has the correct dimensions
        2. It contains only valid symbols (X, O, or empty)
        3. The number of X's and O's is valid (their difference is 0 or 1)

        Args:
            board (List[List[str]]): The board to check.

        Returns:
            bool: True if the board is valid, False otherwise.
        """

    def _count_moves(self, board) -> Tuple[Optional[int], Optional[int]]:
        """
        Count the number of moves made by each player on the given board and
        updates the instance variables self._x_count and self._o_count 
        accordingly, if the board only contains valid symbols.

        Args:
            board (List[List[str]]): The 2D list representing the board state to 
                count moves from.

        Returns:
            Tuple[Optional[int], Optional[int]]: A tuple containing the count 
                of X moves and O moves. If the board contains invalid symbols,
                it returns (None, None).

        """

    def reset(self) -> None:
        """Reset the game to its initial state."""

    # ==========================================================================
    # Making moves
    # ==========================================================================

    def make_move(self, row: int, col: int) -> bool:
        """
        Make a move on the board.

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.

        Returns:
            bool: True if the move is valid and made, False otherwise.
        """

    def _is_valid_move(self, row: int, col: int) -> bool:
        """
        Get a list of all valid moves.

        Returns:
            List[Tuple[int, int]]: List of (row, col) tuples representing valid moves.
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

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Return a list of all valid moves.
        """

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

        Args:
            board (AbstractBoard): The game board.

        Returns:
            Optional[str]: The winner ('X' or 'O') or None if there is no winner.
        """

    # ==========================================================================
    # Displaying the board
    # ==========================================================================
    def __str__(self) -> str:
        """
        Get the string representation of the current state of the board.

        Returns:
            str: The string representation of the board.
        """

    def print_board(self) -> None:
        """
        Print the string representation of the current state of the board.
        """

    # ==========================================================================
    # Properties
    # ==========================================================================

    @property
    def size(self) -> int:
        """
        Get the size of the board.

        Returns:
            int: The size of the board.
        """

    @property
    def current_player(self) -> Player:
        """
        Get the current player.

        Returns:
            Player: The current player (Player.X or Player.O).
        """

    @property
    def winner(self) -> Optional[Player]:
        """
        Get the winner of the game.

        Returns:
            Optional[Player]: The winner (Player.X or Player.O) or None if there is no winner yet.
        """
