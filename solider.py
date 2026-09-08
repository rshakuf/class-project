import pygame
import consts
import curses

player= curses.initscr()
def print_char (x,y,char):
    player.addch(y,x,char)

if __name__=="__main__":

    print_char(consts.SOLDIER_ROWS,consts.SOLDIER_COLS, 4)
    # SOLDIER_ROWS = 4
    # SOLDIER_COLS = 2
    # SOLDIER_BODY_ROWS = 3  # the upper part
    # SOLDIER_FEET_ROWS = 1