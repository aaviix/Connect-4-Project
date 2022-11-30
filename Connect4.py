import numpy as np
import pygame
import sys
import math

#GAME COLOR SCHEME
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
light_blue = (60, 164, 228)

#COUNT OF ROWS AND COLUMNS
row_count = 6
column_count = 7

#DIPLAY SIZE
dis_width = 700
dis_height = 700
mainWindow = pygame.display.set_mode((dis_width, dis_height))
mainWindow.fill(light_blue)
pygame.display.set_caption('Connect 4 Game by Patel Dhruv')

#CREATING THE GAME BOARD
def create_board():
    board = np.zeros((row_count, column_count))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[row_count - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

#PRINTING THE GAME BOARD
def print_board(board):
    print(np.flip(board, 0))

#DEFINING THE GAME INPUTS
def winning_move(board, piece):
    #CHECKING HORIZONTAL LOCATION FOR WIN
    for c in range(column_count - 3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    #CHECKING VERTICAL LOCATION FOR WIN
    for c in range(column_count):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    #CHECK POSITIVTLY SLOPE DIAGONALS
    for c in range(column_count - 3):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    #CHECK NEGATIVTLY SLOPE DIAGONALS
    for c in range(column_count - 3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True

#DEFINING THE GAME BOARD COLOR SCHEME
def draw_board(board):
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.rect(screen, yellow, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, light_blue, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(column_count):
        for r in range(row_count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, black, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0

# INITIALIZE GAME
pygame.init()

# DEFINING SCREEN SIZE
SQUARESIZE = 100

# DEFINING THE WIDTH AND HEIGHT OF BOARD
width = column_count * SQUARESIZE
height = (row_count + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
screen.fill(light_blue)

# CALLING FUNCTION AGAIN draw_board
draw_board(board)
pygame.display.update()

# DEFINING THE FONT
myfont = pygame.font.SysFont("timeroman", 50)

# GAME SETUP
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, light_blue, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, black, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, light_blue, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # ASK FOR PLAYER 1 INPUT
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, red)
                        screen.blit(label, (40, 10))
                        game_over = True


            # ASK FOR PLAYER 2 INPUT
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, black)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
