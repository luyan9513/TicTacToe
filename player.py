import math
import random


class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # position = -1
        # available_moves = game.available_move()
        # while True:
        #     print(f"The available moves are {available_moves}")
        #     position = int(input("Enter you move: "))
        #     if position not in game.available_move():
        #         print("Invalid move, please try again: ")
        #     else:
        #         break
        # return position
        position = None
        valid_move = False
        while not valid_move:
            print(f"The available moves are {game.available_move()}")
            user_input = input(f"{self.letter}'s turn. Enter you move: ")
            try:
                position = int(user_input)
                if position not in game.available_move():
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Invalid move, try again.")
        return position


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_move())


class AIComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_move()) == 9:
            position = random.choice(game.available_move())
        else:
            position = self.minimax(game, self.letter)["position"]
        return position

    def minimax(self, game, player):
        max_player = self.letter
        other_player = "O" if max_player == "X" else "X"

        if game.current_winner == other_player:
            return {
                "position": None,
                "score": game.num_empty_squares() + 1
                if other_player == max_player
                else (-1) * (game.num_empty_squares() + 1),
            }
        elif not game.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}
        else:
            best = {"position": None, "score": math.inf}

        for possible_move in game.available_move():
            game.make_move(possible_move, player)
            sim = self.minimax(game, other_player)

            game.board[possible_move] = " "
            game.current_winner = None
            sim["position"] = possible_move

            if player == max_player:
                if sim["score"] > best["score"]:
                    best = sim
            else:
                if sim["score"] < best["score"]:
                    best = sim

        return best
