"""
TicTacToeGame Module

This module implements a simple 4x4 Tic-Tac-Toe game with options for human 
vs human and human vs AI gameplay. It also includes tournament functionality.
"""

import time
import random
from typing import Tuple, Dict
from enums import Player, GameState
from tic_tac_toe_4x4 import TicTacToe4x4


class TicTacToeGame:
    """
    Manages the Tic-Tac-Toe game, including game setup, gameplay, and tournaments.
    """
    def __init__(self):
        """Initialize the TicTacToeGame with a new board and empty AI player."""
        self.game = TicTacToe4x4()
        self.ai_player = None

    def play_game(self, ai_game: bool = True, ai_starts: bool = False) -> None:
        """
        Play a single game of Tic-Tac-Toe.

        Args:
            ai_game (bool): If True, one player is AI. If False, both players are human.
            ai_starts (bool): If True and ai_game is True, AI plays first.
        """
        print("Welcome to 4x4 Tic-Tac-Toe!")
        self.game.reset()
        if ai_game:
            self.ai_player = Player.X if ai_starts else Player.O

        while self.game.get_game_state() == GameState.ONGOING:
            self.game.print_board()
            current_player = self.game.current_player

            if ai_game and current_player == self.ai_player:
                move = self._ai_move()
                print(f"AI ({current_player.value}) chose: {move}")
            else:
                move = self._human_move(current_player)

            self.game.make_move(*move)

        self._display_game_result()

    def _human_move(self, player: Player) -> Tuple[int, int]:
        """
        Get a valid move from the human player.

        Args:
            player (Player): The current player (X or O).

        Returns:
            Tuple[int, int]: The chosen (row, column) move.
        """
        while True:
            try:
                print(f"Player {player.value}'s turn")
                row = int(input(f"Enter row (0-{self.game.size-1}): "))
                col = int(input(f"Enter column (0-{self.game.size-1}): "))
                if 0 <= row < self.game.size and 0 <= col < self.game.size:
                    if self.game.make_move(row, col):
                        return row, col
                    print("That position is already occupied. Try again.")
                else:
                    print(
                        f"Invalid input. Please enter numbers between 0 and {self.game.size-1}."
                    )
            except ValueError:
                print("Invalid input. Please enter numbers.")

    def _ai_move(self) -> Tuple[int, int]:
        """
        Generate a move for the AI player.

        Returns:
            Tuple[int, int]: The chosen (row, column) move.
        """
        print("AI is thinking...")
        time.sleep(0.5)  # Simulate AI thinking
        return random.choice(self.game.valid_moves)

    def _display_game_result(self) -> None:
        """Display the final game board and result."""
        self.game.print_board()
        print(f"Game over! Result: {self.game.get_game_state().value}")

    def play_tournament(
        self, num_games: int = 10, human_vs_human: bool = False
    ) -> None:
        """
        Play a tournament of multiple games and report statistics.

        Args:
            num_games (int): Number of games to play in the tournament.
            human_vs_human (bool): If True, all games are human vs human.
        """
        results: Dict[GameState, int] = {
            state: 0 for state in GameState if state != GameState.ONGOING
        }

        for i in range(num_games):
            print(f"\n{'='*10} Game {i+1} of {num_games} {'='*10}")
            self.play_game(ai_game=not human_vs_human, ai_starts=i % 2 == 0)
            results[self.game.get_game_state()] += 1

        self._display_tournament_results(results)

    def _display_tournament_results(self, results: Dict[GameState, int]) -> None:
        """
        Display the results of a tournament.

        Args:
            results (Dict[GameState, int]): Dictionary of game results and their counts.
        """
        print("\nTournament Results:")
        for state, count in results.items():
            print(f"{state.value}: {count}")


def main():
    """Main function to run the Tic-Tac-Toe game."""
    game = TicTacToeGame()
    while True:
        choice = display_main_menu()
        if choice == 1:
            game_tournament_menu(game, single=True)
        elif choice == 2:
            game_tournament_menu(game, single=False)
        elif choice == 3:
            exit_game()
        else:
            print("Invalid choice. Please try again.")


def display_main_menu() -> int:
    """Display the main menu and return the user's choice."""
    print("\nTic Tac Toe Main Menu:")
    print("1. Single Player (vs AI)")
    print("2. Multiplayer (Human vs Human)")
    print("3. Exit")
    return get_menu_choice(3)


def game_tournament_menu(game: TicTacToeGame, single: bool):
    """Handle the single player (vs AI) menu."""

    while True:
        print(
            "\n{mode} Menu:".format(
                mode="Single Player vs. AI" if single else "Multiplayer"
            )
        )
        print("1. Play a single game")
        print("2. Play a tournament")
        print("3. Return to main menu")
        choice = get_menu_choice(3)

        if choice == 1:
            if single:
                ai_starts = input("Should AI start? (y/n): ").lower().startswith("y")
                game.play_game(ai_game=True, ai_starts=ai_starts)
            else:
                game.play_game(ai_game=False)
        elif choice == 2:
            play_tournament_menu(game, human_vs_human=False if single else True)
        elif choice == 3:
            return
        else:
            print("Invalid choice. Please try again.")


def play_tournament_menu(game: TicTacToeGame, human_vs_human: bool):
    """Handle the logic for playing a tournament."""
    try:
        num_games = int(input("Enter the number of games for the tournament: "))
        game.play_tournament(num_games, human_vs_human=human_vs_human)
    except ValueError:
        print("Invalid input. Please enter a valid number of games.")


def get_menu_choice(max_choice: int) -> int:
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = int(input(f"Enter your choice (1-{max_choice}): "))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(
                    f"Invalid choice. Please enter a number between 1 and {max_choice}."
                )
        except ValueError:
            print("Invalid input. Please enter a number.")


def exit_game():
    """Handle the game exit."""
    print("Thanks for playing!")
    exit()


if __name__ == "__main__":
    main()
