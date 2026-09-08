import pygame
import sys
import random
import consts
import game_field
img = pygame.image.load('mine.png')
# image = pygame.transform.scale(img, (int(10* 0.5), int(10 * 0.5)))
image=pygame.transform.scale(img,(50,50))
def create_board ():
    screen = pygame.display.set_mode( (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT) )

    surface = pygame.surface.Surface(screen.get_size()).convert_alpha()
    surface.fill([0,0,0,0])
    # pygame.draw.polygon(surface, consts.RED, [(100,100), (200,200), (300,100)])

    clock = pygame.time.Clock()

    running = True
    while running:

        # --- events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- draws ---

        screen.fill(consts.BLACK)

        # for i in range(len(game_field.matrix())):
        #     t = game_field.matrix()[i]
        #     screen.blit(image,t[i], t[i])



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

if __name__=="__main__":
    create_board()