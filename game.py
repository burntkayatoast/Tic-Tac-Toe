from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board= Board() #instance to manage game board
        self.players = [
            Player(input("Name for player 1 (X): "), "X"),
            Player(input("Name for player 2 (O): "), "O"),
        ]
        self. cur_player = 0 #tracks whose turn it is

    def play_game(self):
            print("\nReady to play Tic Tac Toe?")
            while 1:
                self.board.board_outline() #displays current board
                player = self.players[self.cur_player] #see whose turn it is.
                print(f"{player.name}'s turn: {player.symbol}") #tells user
                # whose turn it is

                try:
                    row, col = map(int, input(
                        "\nEnter row and column (1-3) separated by space\ne.g "
                        "for Row 1, Column 1, enter 1 1: "
                        "").split())
                    #winner winner chicken dinner
                    if self.board.update(row, col, player.symbol):
                        if self.board.check_win(player.symbol):
                            self.board.board_outline()
                            print(f"Congratulations, {player.name} wins!")
                            break
                        elif self.board.is_complete():
                            self.board.board_outline()
                            print("It's a draw!")
                            break
                        self.cur_player = 1 - self.cur_player
                    else:
                        print("Invalid move, try again.") #invalid move
                except (ValueError, IndexError):
                    print("Please enter valid row and column numbers (1-3).")
