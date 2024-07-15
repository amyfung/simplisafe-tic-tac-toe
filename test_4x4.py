import unittest
from typing import List, Tuple
from tic_tac_toe_4x4 import TicTacToe4x4
from enums import Player, GameState

class TestTicTacToe4x4(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe4x4()

    # ==========================================================================
    # Initialization tests
    # ==========================================================================
    def test_initialization(self):
        """Test the initialization of the game."""
        self.assertEqual(self.game.size, 4, "Board size should be 4x4")
        self.assertEqual(self.game._x_count, 0, "Player X should have made no moves")
        self.assertEqual(self.game._o_count, 0, "Player O should have made no moves")
        self.assertEqual(self.game.current_player, Player.X, "First player should be X")
        self.assertIsNone(self.game._winner, "There should be no winner at start")
        self.assertEqual(len(self.game._empty_cells), 16, "All cells should be empty at start")
        self.assertEqual(self.game.game_state, GameState.ONGOING, "Game state should be ONGOING at start")

    def test_valid_initialization_with_existing_board(self):
        """Test initialization with valid existing board states."""
        valid_boards = [
            [
                ["X", "O", "", ""],
                ["", "X", "", ""],
                ["", "", "O", ""],
                ["", "", "", ""],
            ],
            [
                ["X", "", "", ""],
                ["O", "X", "", ""],
                ["", "O", "X", ""],
                ["", "", "O", ""],
            ],
        ]
        for board in valid_boards:
            with self.subTest(board=board):
                game = TicTacToe4x4(initial_state=board)
                self.assertEqual(game.size, 4, "Board size should remain 4x4")
                self.assertIsNone(game._winner, "There should be no winner for this valid board")
                self.assertGreater(len(game._empty_cells), 0, "This board should not be full")

    def test_initialization_with_current_player(self):
        """Test initialization with specified current player."""
        board = [
            ["X", "O", "", ""],
            ["", "X", "", ""],
            ["", "", "O", ""],
            ["", "", "", ""],
        ]
        game = TicTacToe4x4(initial_state=board, current_player=Player.X)
        self.assertEqual(game.current_player, Player.X, "Current player should be X")
        
        game = TicTacToe4x4(initial_state=board, current_player=Player.O)
        self.assertEqual(game.current_player, Player.O, "Current player should be O")
            
        board_inconsistent = [
            ["X", "O", "", ""],
            ["", "X", "", "O"],
            ["", "", "O", ""],
            ["", "", "", ""],
        ]
        with self.assertRaises(ValueError, msg="Should raise ValueError for inconsistent current player"):
            TicTacToe4x4(initial_state=board_inconsistent, current_player=Player.O)

    def test_invalid_board_state(self):
        """Test initialization with invalid board states."""
        invalid_states = [
            [["", "X", "X"], ["O", "O", ""], ["", "", ""]],  # Incorrect size
            [["X", "O", "", ""], ["", "X", "", ""], ["", "A", "O", ""], ["", "", "", ""]],  # Invalid character
            [["X", "O", "X", "X"], ["X", "X", "X", "X"], ["O", "X", "O", "X"], ["X", "X", "X", "X"]],  # Too many X moves
            [["X", "O", "X", "O"], ["X", "O", "O", "X"], ["O", "X", "O", "O"], ["O", "O", "O", "O"]],  # Too many O moves
        ]

        for state in invalid_states:
            with self.assertRaises(ValueError, msg=f"Should raise ValueError for invalid state: {state}"):
                TicTacToe4x4(initial_state=state)

    def test_x_and_o_count_with_initial_state(self):
        """Test that _x_count and _o_count are accurate when initializing with a board state."""
        initial_states = [
            ([
                ["X", "O", "", ""],
                ["", "X", "", ""],
                ["", "", "O", ""],
                ["", "", "", ""],
            ], 2, 2),
            ([
                ["X", "O", "X", ""],
                ["O", "X", "", ""],
                ["", "", "O", "X"],
                ["", "", "", ""],
            ], 4, 3),
            ([
                ["X", "O", "X", "O"],
                ["O", "X", "O", "X"],
                ["X", "O", "X", "O"],
                ["", "", "", ""],
            ], 6, 6),
        ]
        
        for board, expected_x_count, expected_o_count in initial_states:
            game = TicTacToe4x4(initial_state=board)
            self.assertEqual(game._x_count, expected_x_count, f"X count should be {expected_x_count} for given board")
            self.assertEqual(game._o_count, expected_o_count, f"O count should be {expected_o_count} for given board")
    
    # ==========================================================================
    # Making moves tests
    # ==========================================================================
    def test_make_move(self):
        """Test making valid and invalid moves."""
        print("Testing making valid and invalid moves")
        self.assertTrue(
            self.game.make_move(0, 0), "Should be able to make a move on an empty cell"
        )
        self.assertEqual(
            self.game.current_player, Player.O, "Player should change after a move"
        )
        self.assertFalse(
            self.game.make_move(0, 0), "Should not be able to move on an occupied cell"
        )
        self.assertFalse(
            self.game.make_move(-1, 0),
            "Should not be able to move outside the board (negative)",
        )
        self.assertFalse(
            self.game.make_move(0, 4),
            "Should not be able to move outside the board (too large)",
        )
        
    def test_get_valid_moves(self):
        """Test getting valid moves."""
        print("Testing getting valid moves")
        self.game.make_move(0, 0)
        valid_moves = self.game.valid_moves
        self.assertEqual(
            len(valid_moves), 15, "Should have 15 valid moves after one move"
        )
        self.assertNotIn(
            (0, 0), valid_moves, "The occupied cell should not be in valid moves"
        )
        
if __name__ == "__main__":
    unittest.main()