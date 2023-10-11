import numpy as np
from typing import Union


class TicTacToe:
    def __init__(self, players, grid_size=3, win_size=3):
        self.grid_size = grid_size
        self.win_size = win_size
        self.grid = np.array([str(x) for x in range(9)]).reshape((grid_size, grid_size))
        self.players = players

        self.current_move = 0
        self.max_moves = self.grid_size * self.grid_size - 1

    def print(self):
        turn = self.current_move % 2
        out_string = ""
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                out_string += str(col)
                if x < self.grid_size - 1:
                    out_string += "|"
            out_string += "\n"
        print(out_string)
        print(f"Player {turn + 1}'s ({self.players[turn]}) Turn!")

    def get_current_player(self):
        return self.players[self.current_move % len(self.players)]

    def play(self, move: Union[int, tuple]):
        if type(move) is tuple:
            x, y = move
        else:
            # Move is a number
            x, y = int(move % self.grid_size), int(move / self.grid_size)

        if self.grid[y, x] in self.players:
            print("Invalid move, please try again")
            return False, None

        self.grid[y, x] = self.get_current_player()
        result = self.evaluate()

        self.current_move += 1
        return result

    def evaluate(self):
        # Using masks is the fun \ unique way, and we are all about learning having fun!
        y, x = np.ogrid[:self.grid_size, :self.grid_size]

        rows = [self.grid[((y == row) & (x >= 0))] for row in range(self.grid_size)]
        cols = [self.grid[((y >= 0) & (x == col))] for col in range(self.grid_size)]

        diag_mask = (x == y)
        diag = self.grid[diag_mask]

        anti_diag_mask = (x + y == self.grid_size - 1)
        anti_diag = self.grid[anti_diag_mask]

        threes = rows+cols+[diag]+[anti_diag]
        unique_threes = [np.unique(three) for three in threes]
        winning_three = [three[0] for three in unique_threes if len(three) == 1]

        if not winning_three:
            if self.current_move >= self.max_moves:
                return True, None
            return False, None

        winner = winning_three[0]
        return True, self.players.index(winner) + 1
