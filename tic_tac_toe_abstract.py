"""
tic_tac_toe_abstract.py

This module defines an abstract base class for a Tic-Tac-Toe game board.
It provides a flexible structure that can be extended to create various
Tic-Tac-Toe game variants of different sizes and winning conditions.

"""

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Set
from enums import Player, GameState

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
    
    # ==========================================================================
    # Initializing the board
    # ==========================================================================
    def __init__(self, size: int, initial_state: Optional[List[List[str]]] = None, current_player: Optional[Player] = None):
        if size < 3:
            raise ValueError("Board size must be at least 3x3")
        
        self._size = size
        self._board: List[List[str]]
        self._empty_cells: Set[Tuple[int, int]]
        self._x_count: int
        self._o_count: int
        self._winner: Optional[Player] = None

        if not initial_state:
            self._initialize_new_board()
            self._current_player = (
                Player.X if current_player is None else current_player
            )
        else:
            self._initialize_from_state(initial_state, current_player)

    def _initialize_new_board(self) -> None:
        """
        Initialize a new empty game board of the specified size, as well as the
        set of empty cells and the move counts for both players.
        """
        self._board = [[''] * self._size for _ in range(self._size)]
        self._x_count= self._o_count = 0
        self._empty_cells = {(r, c) for r in range(self._size) for c in range(self._size)}

    def _initialize_from_state(self, initial_state: List[List[str]], current_player: Optional[Player]) -> None:
        """
        Initialize the game board from a given initial state.

        This method sets up the board based on the provided initial state,
        validates the state, and initializes game counters and the current player.

        Raises:
            ValueError: If the initial board state is invalid.
        """
        if not self._is_valid_board(initial_state):
            raise ValueError("Invalid initial board state")

        self._board = initial_state
        self._empty_cells = {(r, c) for r in range(self._size) for c in range(self._size) if not initial_state[r][c]}
        self._x_count, self._o_count = self._count_moves(self._board)
        
        if current_player is None:
            self._current_player = Player.X if self._x_count <= self._o_count else Player.O
        elif (current_player == Player.X and self._x_count > self._o_count) or \
             (current_player == Player.O and self._o_count > self._x_count):
            raise ValueError("Provided current player is inconsistent with the board state")
        else:
            self._current_player = current_player

        self._winner = self.check_winner()


    def _is_valid_board(self, state) -> bool:
        """
        Check if the board state is valid.

        Returns:
            bool: True if the board state is valid, False otherwis\e.
        """
        # Check board dimensions
        if len(state) != self.size or any(len(row) != self.size for row in state):
            return False

        # Count moves and check for validity
        x_count, o_count = self._count_moves(state)
        return x_count and abs(x_count - o_count) <= 1

    def _count_moves(self, board) -> Tuple[Optional[int], Optional[int]]:
        """
        Count the number of moves made by each player.

        Returns:
            Tuple[Optional[int], Optional[int]]: A tuple containing the count of X and O moves.
                Returns (None, None) if an invalid symbol is found on the board.
        """
        x_count = o_count = 0
        for row in board:
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
        self._current_player = Player.X
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
        if not self._is_valid_move(row, col):
            return False

        self._board[row][col] = self._current_player.value
        self._empty_cells.remove((row, col))
        
        if self._current_player == Player.X:
            self._x_count += 1
        else:
            self._o_count += 1

        if self.is_winning_move(row, col):
            self._winner = self._current_player

        self._current_player = (
            Player.O if self._current_player == Player.X else Player.X
        )
        return True

    def _is_valid_move(self, row: int, col: int) -> bool:
        """
        Check if a move is valid (i.e., the cell is empty).

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return ((row, col) in self._empty_cells)

    # ==========================================================================
    # Solver methods that check the game state
    # ==========================================================================
    
    def is_game_over(self) -> bool:
        """
        Check whether the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return bool(self._winner) or not self.any_moves_left()

    def get_game_state(self) -> GameState:
        """
        Get the current game state.

        Returns:
            GameState: The current state of the game.
        """
        if self._winner == Player.X:
            return GameState.X_WINS
        elif self._winner == Player.O:
            return GameState.O_WINS
        elif self._o_count + self._x_count == self._size**2:
            return GameState.DRAW
        return GameState.ONGOING

    def any_moves_left(self) -> bool:
        """
        Check whether there are any moves left.

        Args:
            board (TicTacToeAbstract): The game board.

        Returns:
            bool: True if there are moves left, False otherwise.
        """
        # return not self._valid_moves
        return (self._o_count + self._x_count) < self._size ** 2
    
    def _pass_turn(self):
        """
        Pass the current player's turn.
        This method is intended for testing purposes only.
        """
        self._current_player = (
            Player.O if self._current_player == Player.X else Player.X
        )

    # ==========================================================================
    # Checking winning
    # ==========================================================================
    @abstractmethod
    def is_winning_move(self, row: int, col: int) -> bool:
        """
        Check whether the last move resulted in a win. Additional winning 
        conditions should be implemented by subclasses, if applicable.

        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.

        Returns:
            bool: True if the move resulted in a win or False otherwise.
        """
        # Too few moves on the board to meet any win condition
        if self._o_count < self._size and self._x_count < self._size:
            return None

        player = self._current_player.value

        # Check row
        if all(self._board[row][i] == player for i in range(self.size)):
            return True

        # Check column
        if sum(self._board[i][col] == player for i in range(self._size)) == self._size:
            return True

        # Check diagonals
        if row == col or row + col == self._size - 1:
            main_diag = sum(self._board[i][i] == player for i in range(self._size))
            anti_diag = sum(self._board[i][self._size-1-i] == player for i in range(self._size))
            if main_diag == self._size or anti_diag == self._size:
                return True

        return False

    @abstractmethod
    def check_winner(self) -> Optional[Player]:
        """
        Checks whether there is a winner of the tic-tac-toe game based on the
        horizontal, vertical, and diagonal win conditions. Returns the winner,
        if any, or None.
        
        Additional winning conditions should be implemented by subclasses, 
        if applicable.

        Returns:
            Optional[str]: The winning player or None, if there is no winner.
        """
        if self._winner:
            return self._winner

        if self._o_count < self._size and self._x_count < self._size:
            return None

        # Check rows and columns simultaneously
        for i in range(self._size):
            if self._board[i][0] and all(self._board[i][j] == self._board[i][0] for j in range(1, self._size)):
                return Player(self._board[i][0])
            if self._board[0][i] and all(self._board[j][i] == self._board[0][i] for j in range(1, self._size)):
                return Player(self._board[0][i])

        # Check diagonals
        if self._board[0][0] and all(self._board[i][i] == self._board[0][0] for i in range(1, self._size)):
            return Player(self._board[0][0])
        if self._board[0][self._size-1] and all(self._board[i][self._size-1-i] == self._board[0][self._size-1] for i in range(1, self._size)):
            return Player(self._board[0][self._size-1])

        return None
    
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
        return self._size
    
    @property
    def current_player(self) -> Player:
        """
        Get the current player.

        Returns:
            Player: The current player (Player.X or Player.O).
        """
        return self._current_player
    
    @property
    def valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get the valid moves left in the game.

        Returns:
            List[Tuple[int, int]]: The remaining valid moves.
        """
        return list(self._empty_cells)
    
    @property
    def winner(self) -> Optional[Player]:
        """
        Get the winner of the game.

        Returns:
            Optional[Player]: The winner (Player.X or Player.O) or None if there is no winner yet.
        """
        return self._winner

    # ==========================================================================
    # Displaying board
    # ==========================================================================

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