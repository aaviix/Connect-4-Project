import numpy as np
from variables import *

class Model:
    def __init__(self):
        self.board = np.zeros((row_count, col_count))
    
    def addPiece(self, row, col, piece):
        self.board[row][col] = piece
    
    def validLocation(self, col):
        return self.board[row_count - 1][col] == 0
    
    def next_open_row(self, col):
        for r in range(row_count):
            if self.board[r][col] == 0:
                return r
    
    def printBoard(self):
        print(np.flip(self.board, 0))