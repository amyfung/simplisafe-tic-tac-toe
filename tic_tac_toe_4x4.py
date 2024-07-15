from typing import Optional, List, Tuple, Union
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

    
    def _check_additional_winning_conditions(self, row: Optional[int] = None, col: Optional[int] = None) -> Optional[Union[Player, bool]]:
        """
        Check for additional winning conditions specific to 4x4 board.

        Args:
            row (Optional[int]): The row index for the move (if checking a specific move).
            col (Optional[int]): The column index for the move (if checking a specific move).

        Returns:
            Optional[Union[Player, bool]]: 
                - If row and col are provided: True if the move resulted in a win, False otherwise.
                - If row and col are not provided: The winning Player if found, None otherwise.
        """
        if row is not None and col is not None:
            # Checking for a specific move (is_winning_move)
            # Check corners
            if (row, col) in self._corners and all(self._board[r][c] == self.current_player.value for r, c in self._corners):
                return True
            
            # Check 2x2 boxes
            return self._is_winning_2x2_move(row, col)
        else:
            # Checking the entire board (check_winner)
            # Check corners
            corner_value = self._board[self._corners[0][0]][self._corners[0][1]]
            if corner_value and all(self._board[r][c] == corner_value for r, c in self._corners):
                return Player(corner_value)
            
            # Check 2x2 boxes
            return self._find_2x2_winner()

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