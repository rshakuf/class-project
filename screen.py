from time import time

import pygame
import sys
import random
import consts
import game_field
from screen2 import bomb_screen
import soldier


def load_images():
    img_grass = pygame.image.load('grass.png')
    image_grass = pygame.transform.scale(img_grass, (50, 50))

    img_soldier = pygame.image.load('soldier.png')
    image_soldier = pygame.transform.scale(img_soldier, (50, 55))

    img_flag = pygame.image.load('flag.png')
    flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
    flag_col = consts.BOARD_COLS - consts.FLAG_COLS
    image_flag = pygame.transform.scale(img_flag, (flag_row, flag_col))

    images = {'grass': image_grass, 'soldier': image_soldier,
              'flag': image_flag}
    return images


images = load_images()
screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

clock = pygame.time.Clock()

x_flag = 940
y_flag = 440
# Create a variable to store the
# velocity of player's movement
velocity = 12

window = None


def create_board():
    global window

    surface = pygame.surface.Surface(screen.get_size()).convert_alpha()
    surface.fill([0, 0, 0, 0])
    # pygame.draw.polygon(surface, consts.RED, [(100,100), (200,200), (300,100)])

    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()

    # create the display surface object
    # of specific dimension.
    window = pygame.display.set_mode(
            (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

    # Add caption in the window
    pygame.display.set_caption('Player Movement')


def run_game():
    create_board()

    show_bombs = False
    game_over = False
    game_over_time = 0
    oldepoch = time()
    run = True
    while run:

        if show_bombs:
            bomb_screen(screen)
            if time() - oldepoch >= 1:
                show_bombs = False
        else:
            run, show_bombs = show_board()
            if show_bombs:
                oldepoch = time()

        if not game_over and soldier.check_collision_with_bomb():
            print("Game Over!")
            game_over = True
            game_over_time = time()

        if game_over:
            draw_message("Game Over!", consts.GAME_OVER_FONT_SIZE,
                         consts.GAME_OVER_COLOR,
                         consts.GAME_OVER_LOCATION)
            if time() - game_over_time >= 2:
                run = False

        ms = clock.tick(consts.FPS)
        # pygame.display.set_caption('{}ms'.format(ms)) # 40ms for 25FPS, 16ms for 60FPS
        fps = clock.get_fps()
        pygame.display.set_caption('FPS: {}'.format(fps))

        pygame.display.flip()
        pygame.display.update()
        clock.tick(consts.FPS)

    pygame.quit()
    quit()


def show_board():
    running = True
    show_bombs = False

    window.fill(consts.BACKGROUND_COLOR)

    window.blit(images['soldier'],
                (soldier.soldier_location[0], soldier.soldier_location[1]))
    window.blit(images['flag'], (x_flag, y_flag))

    for i in range(consts.BUSH):
        screen.blit(images['grass'], (consts.li[i], consts.li2[i]))

    for i in range(consts.BUSH):
        screen.blit(images['grass'], (consts.li[i], consts.li2[i]))

    draw_welcome()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if soldier.soldier_location[0] > 0:
                    soldier.soldier_location[0] -= velocity

            if event.key == pygame.K_RIGHT:
                if soldier.soldier_location[0] < consts.WINDOW_WIDTH - images[
                    'soldier'].get_width():
                    soldier.soldier_location[0] += velocity

            if event.key == pygame.K_UP:
                if soldier.soldier_location[1] > 0:
                    soldier.soldier_location[1] -= velocity

            if event.key == pygame.K_DOWN:
                if soldier.soldier_location[1] < consts.WINDOW_HEIGHT - images[
                    'soldier'].get_height():
                    soldier.soldier_location[1] += velocity

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_bombs = True

    return running, show_bombs


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_welcome():
    message = consts.WELCOME_TEXT[0]
    draw_message(message, consts.WELCOME_FONT_SIZE, consts.WELCOME_COLOR,
                 consts.WELCOME_LOCATION1)
    message = consts.WELCOME_TEXT[1]
    draw_message(message, consts.WELCOME_FONT_SIZE, consts.WELCOME_COLOR,
                 consts.WELCOME_LOCATION2)


if __name__ == "__main__":
    game_field.create_bomb_board()
    run_game()
