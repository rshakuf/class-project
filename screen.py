import pygame
import sys
import random
import consts
img = pygame.image.load('grass.png')
# image = pygame.transform.scale(img, (int(10* 0.5), int(10 * 0.5)))
image=pygame.transform.scale(img,(50,50))


screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


# img1=pygame.image.load('soldier.png')
# image=pygame.transform.scale(img1,(50,55))
def create_board ():
    screen = pygame.display.set_mode( (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT) )

    surface = pygame.surface.Surface(screen.get_size()).convert_alpha()
    surface.fill([0,0,0,0])
    # pygame.draw.polygon(surface, consts.RED, [(100,100), (200,200), (300,100)])

    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()

    # create the display surface object
    # of specific dimension.
    window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

    # Add caption in the window
    pygame.display.set_caption('Player Movement')

    # Add player sprite
    img1=pygame.image.load('soldier.png')
    image=pygame.transform.scale(img1,(50,55))
    # game_field.py
    flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
    flag_col = consts.BOARD_COLS - consts.FLAG_COLS

    img2 = pygame.image.load('flag.png')
    # image2 = pygame.transform.scale(img2, (50, 55))
    image2 = pygame.transform.scale(img2, (flag_row, flag_col))

    # image = pygame.image.load("soldier.png")

    # Store the initial
    # coordinates of the player in
    # two variables i.e. x and y.
    x = 10
    y = 10

    x2 = 940
    y2 = 440
    # Create a variable to store the
    # velocity of player's movement
    velocity = 12

    # Creating an Infinite loop
    run = True
    while run:

        # Filling the background with
        # green color
        window.fill(consts.BACKGROUND_COLOR)

        # Display the player sprite at x
        # and y coordinates
        window.blit(image, (x, y))


        window.blit(image2, (x2, y2))
        # iterate over the list of Event objects
        # that was returned by pygame.event.get()
        # method.
        for event in pygame.event.get():
            draw_welcome()
            # Closing the window and program if the
            # type of the event is QUIT
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- draws ---

        screen.fill(consts.GREEN)
        for i in range(consts.BUSH):
            screen.blit(image, (consts.li[i],consts.li2[i]))


        for i in range(consts.BUSH):
            screen.blit(image, (consts.li[i], consts.li2[i]))


        pygame.display.flip()

        # --- FPS ---

        ms = clock.tick(consts.FPS)
        #pygame.display.set_caption('{}ms'.format(ms)) # 40ms for 25FPS, 16ms for 60FPS
        fps = clock.get_fps()
        pygame.display.set_caption('FPS: {}'.format(fps))

    # --- end ---
    # running = 1
    # while running:
    #     screen.fill((consts.GREEN))
    #     screen.blit(img, (0, 0))
    #     pygame.display.flip()

    pygame.quit()
            run = False
            pygame.quit()
            quit()

            # Checking event key if the type
            # of the event is KEYDOWN i.e.
            # keyboard button is pressed
            if event.type == pygame.KEYDOWN:

                # Decreasing the x coordinate
                # if the button pressed is
                # Left arrow key
                if event.key == pygame.K_LEFT:
                    x -= velocity


                # Increasing the x coordinate
                # if the button pressed is
                # Right arrow key
                if event.key == pygame.K_RIGHT:
                    x += velocity

                # Decreasing the y coordinate
                # if the button pressed is
                # Up arrow key
                if event.key == pygame.K_UP:
                    y -= velocity

                # Increasing the y coordinate
                # if the button pressed is
                # Down arrow key
                if event.key == pygame.K_DOWN:
                    y += velocity

            # Draws the surface object to the screen.
            pygame.display.update()


    # img2 = pygame.image.load('flag.png')
    # image2= pygame.transform.scale(img2, (50, 55))
    # x2 = 100
    # y2 = 100
    # window.blit(image2, (x2, y2))

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








if __name__=="__main__":
    create_board()
    # draw_welcome()



