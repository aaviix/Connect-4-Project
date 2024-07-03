#general variables
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
light_blue = (60, 164, 228)

row_count = 6
col_count = 7

SqSize = 100
width = col_count * SqSize
height = (row_count + 1) * SqSize
size = (width, height)
radius = int(SqSize / 2 - 5)
winLength = 4

#ai variables
EMPTY = 0
player = 1
AI = 2

#controller variable
game_over = False