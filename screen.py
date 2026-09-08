import pygame
import sys
import random
import consts


screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


# img1=pygame.image.load('soldier.png')
# image=pygame.transform.scale(img1,(50,55))
def create_board ():
    # screen = pygame.display.set_mode( (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT) )
    #
    # surface = pygame.surface.Surface(screen.get_size()).convert_alpha()
    # surface.fill([0,0,0,0])
    # # pygame.draw.polygon(surface, consts.RED, [(100,100), (200,200), (300,100)])
    #
    # clock = pygame.time.Clock()
    #
    # running = True
    # while running:
    #
    #     # --- events ---
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #         elif event.type == pygame.KEYUP:
    #             if event.key == pygame.K_ESCAPE:
    #                 running = False
    #
    #     # --- draws ---
    #
    #     screen.fill(consts.BACKGROUND_COLOR)
    #
    #     # SOLDIER_ROWS = 4
    #     # SOLDIER_COLS = 2
    #
    #
    #     # screen.blit(image, (2,20))
    #     # rect = img1.get_rect()
    #     # rect = rect.move((consts.SOLDIER_ROWS+400,consts.SOLDIER_COLS))
    #     # screen.blit(img1, rect)
    #
    #
    #     pygame.display.flip()
    #
    #     # --- FPS ---
    #
    #     ms = clock.tick(consts.FPS)
    #     #pygame.display.set_caption('{}ms'.format(ms)) # 40ms for 25FPS, 16ms for 60FPS
    #     fps = clock.get_fps()
    #     pygame.display.set_caption('FPS: {}'.format(fps))
    #
    # # --- end ---
    #
    # pygame.quit()

    # # Initialize Pygame
    # pygame.init()
    #
    # # Set up the game window
    # screen_width, screen_height = 800, 600
    # screen = pygame.display.set_mode((screen_width, screen_height))
    # pygame.display.set_caption("Image Character Movement")
    #
    # # Load character image (create a simple colored surface if no image available)
    # try:
    #     character_img = pygame.image.load("solider.png")
    # except:
    #     # Create a simple colored rectangle as character
    #     character_img = pygame.Surface((50, 50))
    #     character_img.fill((200, 0, 0))  # Red color
    #
    # # character_rect = character_img.get_rect()
    # # character_rect.center = (screen_width // 2, screen_height // 2)
    #
    # # Movement speed
    # movement_speed = 5
    #
    # # Colors
    # WHITE = (255, 255, 255)
    #
    # # Game clock
    # clock = pygame.time.Clock()
    # FPS = 60
    #
    # # Game loop
    # running = True
    # while running:
    #     # Handle events
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #     # Get pressed keys
    #     keys = pygame.key.get_pressed()
    #
    #     # Move character with boundary checking
    #     if keys[pygame.K_LEFT] and character_img.left > 0:
    #         character_img.x -= movement_speed
    #     if keys[pygame.K_RIGHT] and character_img.right < screen_width:
    #         character_img.x += movement_speed
    #     if keys[pygame.K_UP] and character_img.top > 0:
    #         character_img.y -= movement_speed
    #     if keys[pygame.K_DOWN] and character_img.bottom < screen_height:
    #         character_img.y += movement_speed
    #
    #     # Clear screen and draw character
    #     screen.fill(WHITE)
    #     screen.blit(character_img)
    #
    #     # Update display
    #     pygame.display.flip()
    #     clock.tick(FPS)
    #
    # # Quit game
    # pygame.quit()

    # Importing pygame module



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



