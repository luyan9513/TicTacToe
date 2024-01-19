import time
from player import HumanPlayer, RandomComputerPlayer, AIComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()  # a 3x3 board
        self.current_winner = None  # keep track of winner

    def print_current_board(self):
        for row in [self.board[i * 3 : i * 3 + 3] for i in range(3)]:
            print("-------------")
            print("| " + " | ".join(row) + " |")
        print("-------------")

    @staticmethod
    def print_board():
        for row in [[str(i + j * 3) for i in range(3)] for j in range(3)]:
            print("-------------")
            print("| " + " | ".join(row) + " |")
        print("-------------")

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]

    def make_move(self, position, letter):
        if self.is_available_move(position):
            # make the move
            self.board[position] = letter

            # check if there is a winner after each move
            if self.winner(position, letter):
                self.current_winner = letter

            return True

        return False

    def winner(self, position, letter):
        # check the row
        row_index = position // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all([x == letter for x in row]):
            return True

        # check the column
        column_index = position % 3
        column = [self.board[column_index + 3 * i] for i in range(3)]
        if all([x == letter for x in column]):
            return True

        # check the diagonal
        if position % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([x == letter for x in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([x == letter for x in diagonal2]):
                return True

        return False

    def is_available_move(self, position):
        return position in self.available_move()

    def available_move(self):
        return [i for (i, x) in enumerate(self.board) if x == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = "X"

    while game.empty_squares():
        if letter == "X":
            position = x_player.get_move(game)
        else:
            position = o_player.get_move(game)

        game.make_move(position, letter)

        if print_game:
            print(f"{letter} make a move to {position}")
            game.print_current_board()
            print()

        if game.current_winner:
            if print_game:
                print(f"Congratulations {letter}! You have won!")
            return letter

        letter = "O" if letter == "X" else "X"

        time.sleep(1)

    if print_game:
        print("It's a tie!")


if __name__ == "__main__":
    x = HumanPlayer("X")
    o = AIComputerPlayer("O")
    g = TicTacToe()
    play(g, x, o)
