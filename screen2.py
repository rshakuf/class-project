import pygame
import sys
import random
import consts
import game_field
import soldier

img = pygame.image.load('mine.png')
# image = pygame.transform.scale(img, (int(10* 0.5), int(10 * 0.5)))
image=pygame.transform.scale(img,(50,50))

img_soldier=pygame.image.load('soldier.png')
image_soldier=pygame.transform.scale(img_soldier,(50,55))


def bomb_screen(screen):
    # --- draws ---

    screen.fill(consts.BLACK)

    screen.blit(image_soldier, (soldier.soldier_location[0], soldier.soldier_location[1]))

    for i in game_field.list_of_mines:
        screen.blit(image, (i[1], i[0]))

