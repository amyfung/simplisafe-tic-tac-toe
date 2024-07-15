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
        super().__init__(4, initial_state, current_player)

    def check_winner(self) -> Optional[Player]:
        """
        Check if there is a winner based on the 4x4 game rules.

        Returns:
            Optional[Player]: The winning player (Player.X or Player.O) or None if there is no winner.
        """
        

    def is_winning_move(self, row: int, col: int) -> bool:
        """
        Check whether the last move resulted in a win based on 4x4 game rules.
        
        Args:
            row (int): The row index for the move.
            col (int): The column index for the move.
        
        Returns:
            bool: True if the move resulted in a win, False otherwise.
        """
        

    