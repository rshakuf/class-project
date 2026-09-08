import random
import itertools
import pygame
import consts
bord = [[0 for _ in range(consts.BOARD_COLS)] for _ in
            range(consts.BOARD_ROWS)]
def matrix():

    # img = pygame.image.load('mine.png')
    # image = pygame.transform.scale(img, (50, 50))
    list_of_mines = []
    for i in range(consts.MINES_COUNT):
        row=random.randint(0, consts.BOARD_ROWS-1)
        col=random.randint(0, consts.BOARD_COLS-1)
        while (row== consts.flag_row and col== consts.flag_col) or (row==consts.SOLDIER_ROWS and col==consts.SOLDIER_COLS):
            row = random.randint(consts.BOARD_ROWS, consts.BOARD_COLS)
            col = random.randint(consts.BOARD_ROWS, consts.BOARD_COLS)
        bord[row][col] = 1
        new_row=row*consts.CELL_SIZE
        new_col=col* consts.CELL_SIZE
        t = (new_row,new_col)
        list_of_mines.append(t)
    # print(bord)
    print(list_of_mines)
    return list_of_mines

        # screen.blit(image, (consts.li[i], consts.li2[i]))



# for row in range(len(bord)):
#     for col in range(len(bord[row])):
         # if row!=consts.flag_col and col!=consts.flag_row:
         #     bord[row][col]=="1"

matrix()
