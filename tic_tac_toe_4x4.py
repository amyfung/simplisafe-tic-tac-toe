from typing import Optional, List, Tuple
from enums import Player
from tic_tac_toe_abstract import TicTacToeAbstract

class TicTacToe4x4(TicTacToeAbstract):
    """
    Concrete class representing a 4x4 tic-tac-toe board.
    This class extends the TicTacToeAbstract to implement the specific winning conditions for a 4x4 game.
    """

    def __init__(
        self,
        initial_state: Optional[List[List[str]]] = None,
        current_player: Optional[Player] = None,
    ):
        """
        Initialize the 4x4 tic-tac-toe board.

        Args:
            initial_state (Optional[List[List[str]]]): The initial state of the board.
            current_player (Optional[Player]): The current player (Player.X or Player.O).

        Raises:
            ValueError: If the initial state is invalid.
        """
        self._corners = [(0, 0), (0, 3), (3, 0), (3, 3)]
        super().__init__(4, initial_state, current_player)

    def check_winner(self) -> Optional[Player]:
        """
        Check if there is a winner based on the 4x4 game rules.

        Returns:
            Optional[Player]: The winning player (Player.X or Player.O) or None if there is no winner.
        """
        # Check standard winning conditions (rows, columns, main diagonals)
        standard_winner = super().check_winner()
        if standard_winner:
            return standard_winner
        
        # Check corners
        corner_value = self._board[self._corners[0][0]][self._corners[0][1]]
        if corner_value and all(self._board[r][c] == corner_value for r, c in self._corners):
            return Player(corner_value)
        
        # Check 2x2 boxes
        return self._find_2x2_winner()

    def is_winning_move(self, row: int, col: int) -> bool:
        """
        Check whether the last move resulted in a win based on 4x4 game rules.
        
        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.
        
        Returns:
            bool: True if the move resulted in a win, False otherwise.
        """
        # Check standard winning conditions
        if super().is_winning_move(row, col):
            return True
        
        player_count = self._x_count if self.current_player == Player.X else self._o_count
        if player_count < self.size:
            return False
        
        # Check corners
        if (row, col) in self._corners and all(self._board[r][c] == self.current_player.value for r, c in self._corners):
            return True
        
        # Check 2x2 boxes
        return self._is_winning_2x2_move(row, col)

    def _find_2x2_winner(self) -> Optional[Player]:
        """
        Find a winner in any 2x2 box on the board.

        Returns:
            Optional[Player]: The winning player if found, None otherwise.
        """
        for i in range(3):
            for j in range(3):
                if self._board[i][j] and self._is_2x2_box_filled(i, j):
                    return Player(self._board[i][j])
        return None

    def _is_winning_2x2_move(self, row: int, col: int) -> bool:
        """
        Check if the move at (row, col) creates a winning 2x2 box.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.

        Returns:
            bool: True if the move creates a winning 2x2 box, False otherwise.
        """
        for i in range(max(0, row-1), min(3, row+1)):
            for j in range(max(0, col-1), min(3, col+1)):
                if self._is_2x2_box_filled(i, j):
                    return True
        return False

    def _is_2x2_box_filled(self, row: int, col: int) -> bool:
        """
        Check if a 2x2 box starting at the given position is filled with the same symbol.

        Args:
            row (int): The starting row index of the 2x2 box.
            col (int): The starting column index of the 2x2 box.

        Returns:
            bool: True if the 2x2 box is filled with the same symbol, False otherwise.
        """
        return len(set(self._board[r][c] for r in range(row, row+2) for c in range(col, col+2))) == 1 and self._board[row][col] != ''