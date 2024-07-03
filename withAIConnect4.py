import numpy as np
import pygame
import random
import sys
import math
from variables import *

#set window
mainWindow = pygame.display.set_mode((700, 700))
mainWindow.fill(light_blue)
pygame.display.set_caption('Connect 4 (With AI version)')


def addPiece(board, row, col, piece):
    board[row][col] = piece

#check if valid location
def validLocation(board, col):
    return board[row_count - 1][col] == 0

def next_open_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

#check if terminal node
def ifTerminal(board):
    return check_win(board, player) or check_win(board, AI) or len(get_validLocation(board)) == 0

def printBoard(board):
    print(np.flip(board, 0))

def draw_line(piece, row, col, ori):
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

#check for win
def check_win(board, piece):
    #horizontal
    for c in range(col_count - 3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                draw_line(piece, r, c, 'horizontal')
                return True

    #vertical
    for c in range(col_count):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                draw_line(piece, r, c, 'vertical')
                return True

    #diagonal 1
    for c in range(col_count - 3):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                draw_line(piece, r, c, 'diagonal1')
                return True

    #diagonal 2
    for c in range(col_count - 3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                draw_line(piece, r, c, 'diagonal2')
                return True

#score evaluation
def evaluate(window, piece):
    score = 0
    opp_piece = player
    if piece == player:
        opp_piece = AI

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def getScore(board, piece):
    score = 0

    #center column
    center_array = [int(i) for i in list(board[:, col_count // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    #horizontal
    for r in range(row_count):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(col_count - 3):
            window = row_array[c:c + winLength]
            score += evaluate(window, piece)

    #vertical
    for c in range(col_count):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(row_count - 3):
            window = col_array[r:r + winLength]
            score += evaluate(window, piece)

    #diagonal 1
    for r in range(row_count - 3):
        for c in range(col_count - 3):
            window = [board[r + i][c + i] for i in range(winLength)]
            score += evaluate(window, piece)

    #diagonal 2
    for r in range(row_count - 3):
        for c in range(col_count - 3):
            window = [board[r + 3 - i][c + i] for i in range(winLength)]
            score += evaluate(window, piece)

    return score

#minmax algorith
def minmax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_validLocation(board)
    is_terminal = ifTerminal(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_win(board, AI):
                return (None, 100000000000000)
            elif check_win(board, player):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            return (None, getScore(board, AI))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_open_row(board, col)
            b_copy = board.copy()
            addPiece(b_copy, row, col, AI)
            new_score = minmax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_open_row(board, col)
            b_copy = board.copy()
            addPiece(b_copy, row, col, player)
            new_score = minmax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def get_validLocation(board):
    valid_locations = []
    for col in range(col_count):
        if validLocation(board, col):
            valid_locations.append(col)
    return valid_locations


#draw game board
def draw_board(board):
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

#main game
while not game_over:
    #create game board
    board = np.zeros((row_count, col_count))
    printBoard(board)

    #initialize game
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(light_blue)
    restart = False
    restartnow = False
    randomMode = False

    #initialize font
    myfont = pygame.font.SysFont('courier new', 30, bold=True, italic=True)

    #draw game board
    draw_board(board)
    pygame.display.update()

    #get random turn
    turn = random.randint(0, 1)

    #game setup
    while not (restart or restartnow):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restartnow = True
                
                if event.key == pygame.K_a:
                    randomMode = True
            
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, light_blue, (0, 0, width, SqSize))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, red, (posx, int(SqSize / 2)), radius)
                else:
                    pygame.draw.circle(screen, black, (posx, int(SqSize / 2)), radius)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, light_blue, (0, 0, width, SqSize))
                #player turn
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SqSize))

                    if validLocation(board, col):
                        row = next_open_row(board, col)
                        addPiece(board, row, col, 1)
                        draw_board(board)

                        if check_win(board, 1):
                            label = myfont.render("Player 1 wins!! GAME OVER", 1, red)
                            screen.blit(label, (5, 5))
                            pygame.display.update()
                            restart = True

                        turn += 1
                        turn = turn % 2

                        printBoard(board)

        #AI turn
        if (turn == 1 and not restart):

            if (randomMode):
                col = random.randint(0, col_count-1)
                print("choosing random column: ", col)
            else:
                col, minmax_score = minmax(board, 5, -math.inf, math.inf, True)
                print("choosing minmax column: ", col)

            if validLocation(board, col):
                row = next_open_row(board, col)
                addPiece(board, row, col, AI)
                draw_board(board)

                if check_win(board, AI):
                    label = myfont.render("AI wins!! GAME OVER", 1, black)
                    screen.blit(label, (5, 5))
                    pygame.display.update()
                    restart = True

                printBoard(board)

                turn += 1
                turn = turn % 2

        if restart:
            pygame.time.wait(3000)
            mainWindow.fill(light_blue)
        
        if restartnow:
            mainWindow.fill(light_blue)
