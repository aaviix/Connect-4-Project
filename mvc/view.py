import pygame
from variables import *

class View:
    def __init__(self):
        pass

    def draw_board(self, board, screen):
        for c in range(col_count):
            for r in range(row_count):
                pygame.draw.rect(screen, yellow, (c * SqSize, r * SqSize + SqSize, SqSize, SqSize))
                pygame.draw.circle(screen, light_blue, (
                int(c * SqSize + SqSize / 2), int(r * SqSize + SqSize + SqSize / 2)), radius)

        for c in range(col_count):
            for r in range(row_count):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, red, (
                    int(c * SqSize + SqSize / 2), height - int(r * SqSize + SqSize / 2)), radius)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, black, (
                    int(c * SqSize + SqSize / 2), height - int(r * SqSize + SqSize / 2)), radius)
        pygame.display.update()
    
    def draw_line(self, screen, piece, row, col, ori):
        color = red if piece % 2 == 0 else black
        start_row = col * 100 + 50
        start_col = (-row + 6) * 100 + 50

        if ori == 'horizontal':
            pygame.draw.line(screen, color, (start_row, start_col), (start_row + 300, start_col), 3)
        
        if ori == 'vertical':
            pygame.draw.line(screen, color, (start_row, start_col), (start_row, start_col - 300), 3)
        
        if ori == 'diagonal1':
            pygame.draw.line(screen, color, (start_row, start_col), (start_row + 300, start_col - 300), 3)
        
        if ori == 'diagonal2':
            pygame.draw.line(screen, color, (start_row, start_col), (start_row + 300, start_col + 300), 3)
