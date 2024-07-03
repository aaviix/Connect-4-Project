import pygame
import sys
import math
from variables import *
from controller import Controller

mainWindow = pygame.display.set_mode((700, 700))
mainWindow.fill(light_blue)
pygame.display.set_caption('Connect 4(PvP using mvc pattern)')

def main():
    while not game_over:

        #initialize game
        pygame.init()
        screen = pygame.display.set_mode(size)
        screen.fill(light_blue)
        restart = False
        restartNow = False
        turn = 0

        game = Controller(screen)
        game.model.printBoard()

        #initialize font
        myfont = pygame.font.SysFont('courier new', 30, bold=True, italic=True)

        #draw game board
        game.view.draw_board(game.model.board, screen)
        pygame.display.update()

        #game setup
        while not (restart or restartNow):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restartNow = True
                
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
                    #player 1 turn
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SqSize))

                        if game.model.validLocation(col):
                            row = game.model.next_open_row(col)
                            game.model.addPiece(row, col, 1)
                            game.view.draw_board(game.model.board, screen)

                            if game.check_win(1):
                                label = myfont.render("Player 1 wins!! GAME OVER", 1, red)
                                screen.blit(label, (5, 5))
                                pygame.display.update()
                                restart = True
                    
                    #player 2 turn
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SqSize))

                        if game.model.validLocation(col):
                            row = game.model.next_open_row(col)
                            game.model.addPiece(row, col, 2)
                            game.view.draw_board(game.model.board, screen)

                            if game.check_win(2):
                                label = myfont.render("Player 2 wins!! GAME OVER", 1, black)
                                screen.blit(label, (5, 5))
                                pygame.display.update()
                                restart = True
                    
                    game.model.printBoard()

                    turn += 1
                    turn = turn % 2

                    if restart:
                        pygame.time.wait(3000)
                        mainWindow.fill(light_blue)
                    
                    if restartNow:
                        mainWindow.fill(light_blue)

if __name__ == '__main__':
    main()