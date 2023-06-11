import pygame
import random

import board
import cards
import dice
import players
import tokens

FPS = 60  # frames per seconds

GREEN = (0,255,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 1080
HEIGHT = 1080
SPAN = WIDTH / 12.2  # TODO: spance may need to be modified; each rolling dice, the token will move: distance = step * span



# initiation and windows
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly")
clock = pygame.time.Clock()


# initiate elements
my_board = board.Board("white")
token1 = tokens.Token("tophat")
token2 = tokens.Token("battleship")
token3 = tokens.Token("boot")
token4 = tokens.Token("racecar")  # TODO: what if less then 4 players

# # picture
# background_img = pygame.image.load(my_board.image_loc).convert()
# background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))


all_sprites = pygame.sprite.Group()
# all_sprites.add(token1)  # TODO: how to keep transparence?
all_sprites.add(token2)
# all_sprites.add(token3)
# all_sprites.add(token4)  # TODO: how to keep transparence?


# game loop
running = True
while running:
    clock.tick(FPS)  # set max. FPS. From loop view, it means this loop will be excuted 60(FPS) times per second.
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if buttd   om "close" in click
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_point = random.randint(1, 3)
                print(f"dice point is {dice_point}.")
                token2.location(dice_point)

    





    # render
    # screen.fill(WHITE)
    screen.blit(my_board.image, (0,0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
