import numpy as np 
class TicTacToe:
    def __init__(self, grid_size = 3  , win_size = 3):
        self.grid_size = grid_size
        self.win_size = win_size

        self.grid = np.array([str(x) for x in range(9)]).reshape((grid_size,grid_size))
        # print(self.grid)
        self.players = ['X','O']
        self.turn = 0

    def print(self): 
        out_string = ""
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                out_string += str(col)
                if x < self.grid_size - 1:
                    out_string += '|'
            out_string += "\n"    
        print(out_string)
           
    def play(self,move:int):
        y,x = int(move/self.grid_size),int(move% self.grid_size)
        if self.grid[y][x] in self.players:
            print("invalid move")
            return
        self.grid[y][x] = self.players[self.turn % 2]
        self.turn += 1

    def evaluate(self):
        y,x = np.ogrid[:self.grid_size,:self.grid_size]
        row =  [self.grid[((y == row) & (x >= 0))] for row in range(self.grid_size)]
        col =  [self.grid[((y >= 0) & (x == col ))] for col in range(self.grid_size)]
        diagonal_mask = (x == y)
        diag = self.grid[diagonal_mask]
        anti_diagonal_maks = (x+y == self.grid_size - 1)
        anti_diag = self.grid[anti_diagonal_maks]

        winner_conditions = row+ col + [diag] + [anti_diag]
        unique_three = [np.unique(three) for three in winner_conditions]
        winning_threes = [three[0] for three in unique_three if len(three) == 1]

        if not winning_threes:
            if self.turn >= self.grid_size**2-1:
                return True,None
            return False, None
        
        winner = winning_threes[0]
        return  True, winner
        

