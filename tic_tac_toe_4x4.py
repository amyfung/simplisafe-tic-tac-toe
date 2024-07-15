from typing import Optional, List, Tuple
from enums import Player
from tic_tac_toe_abstract import TicTacToeAbstract

class TicTacToe4x4(TicTacToeAbstract):
    """
    Concrete class representing a 4x4 tic-tac-toe board.
    This class extends the TicTacToeAbstract to implement the specific winning 
    conditions for a 4x4 game.
    """

    def __init__(
        self,
        initial_state: Optional[List[List[str]]] = None,
        current_player: Optional[Player] = None,
    ):
        """
        Initialize the 4x4 tic-tac-toe board.

        Args:
            initial_state (Optional[List[List[str]]]): The state of an existing
                board, if any.
            current_player (Optional[Player]): The current player (Player.X or 
                Player.O).

        Raises:
            ValueError: If the initial state is invalid.
        """
        self._corners = [(0, 0), (0, 3), (3, 0), (3, 3)]
        super().__init__(4, initial_state, current_player)

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
        
        player_value = self._current_player.value
        
        # Check corners
        if (row, col) in self._corners and all(self._board[r][c] == player_value for r, c in self._corners):
            return True
        
        # Check 2x2 boxes
        for i in range(max(0, row-1), min(3, row)):
            for j in range(max(0, col-1), min(3, col)):
                if (self._board[i][j] == self._board[i][j+1] == 
                    self._board[i+1][j] == self._board[i+1][j+1] == player_value):
                    return True
        
        return False
    
    def check_winner(self) -> Optional[Player]:
        """
        Check whether there is a winner based on the 4x4 game rules.

        Returns:
            Optional[Player]: The winning player (Player.X or Player.O) or None if there is no winner.
        """
        # Check standard winning conditions (rows, columns, main diagonals)
        standard_winner = super().check_winner()
        if standard_winner:
            return standard_winner
        
        # Check corners
        corner_value = self._board[0][0]
        if corner_value and all(self._board[r][c] == corner_value for r, c in self._corners):
            return Player(corner_value)
        
        # Check 2x2 boxes
        for i in range(3):
            for j in range(3):
                if self._board[i][j]:
                    if (self._board[i][j] == self._board[i][j+1] == 
                        self._board[i+1][j] == self._board[i+1][j+1]):
                        return Player(self._board[i][j])

        return None
        

    