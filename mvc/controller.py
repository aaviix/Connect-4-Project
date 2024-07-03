from model import Model
from view import View
from variables import *

class Controller:
    def __init__(self, screen):
        self.model = Model()
        self.view = View()
        self.screen = screen

    def check_win(self, piece):
        #horizontal
        for c in range(col_count - 3):
            for r in range(row_count):
                if self.model.board[r][c] == piece and self.model.board[r][c + 1] == piece and self.model.board[r][c + 2] == piece and self.model.board[r][
                    c + 3] == piece:
                    self.view.draw_line(self.screen, piece, r, c, 'horizontal')
                    return True
        
        #vertical
        for c in range(col_count):
            for r in range(row_count - 3):
                if self.model.board[r][c] == piece and self.model.board[r + 1][c] == piece and self.model.board[r + 2][c] == piece and self.model.board[r + 3][
                    c] == piece:
                    self.view.draw_line(self.screen, piece, r, c, 'vertical')
                    return True

        #diagonal 1
        for c in range(col_count - 3):
            for r in range(row_count - 3):
                if self.model.board[r][c] == piece and self.model.board[r + 1][c + 1] == piece and self.model.board[r + 2][c + 2] == piece and self.model.board[r + 3][
                    c + 3] == piece:
                    self.view.draw_line(self.screen, piece, r, c, 'diagonal1')
                    return True

        #diagonal 2
        for c in range(col_count - 3):
            for r in range(3, row_count):
                if self.model.board[r][c] == piece and self.model.board[r - 1][c + 1] == piece and self.model.board[r - 2][c + 2] == piece and self.model.board[r - 3][
                    c + 3] == piece:
                    self.view.draw_line(self.screen, piece, r, c, 'diagonal2')
                    return True