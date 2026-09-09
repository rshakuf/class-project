import random
import itertools
import pygame
import consts
bomb_board = [[0 for _ in range(consts.BOARD_COLS)] for _ in
            range(consts.BOARD_ROWS)]
list_of_mines = []



def create_bomb_board():
    global bomb_board

    # img = pygame.image.load('mine.png')
    # image = pygame.transform.scale(img, (50, 50))
    for i in range(consts.MINES_COUNT-1):
        row=random.randint(0, consts.BOARD_ROWS-1)
        col=random.randint(0, consts.BOARD_COLS-1)
        while (row == consts.Y_FLAG and col == consts.X_FLAG) or (
                row == consts.SOLDIER_Y and col == consts.SOLDIER_X):
                row = random.randint(0, consts.BOARD_COLS-1)
                col = random.randint(0, consts.BOARD_COLS-1)
        bomb_board[row][col] = 1
        new_row=row*consts.CELL_SIZE
        new_col=col* consts.CELL_SIZE
        t = (new_row,new_col)
        list_of_mines.append(t)
    # print(bord)
    print(list_of_mines)
    #return list_of_mines



# create_matrix()
