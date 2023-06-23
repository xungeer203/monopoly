import pygame
import random

import constants
import board
import cards
import dice
import players
import tokens

FPS = constants.FPS

GREEN = constants.GREEN
RED = constants.RED
BLUE = constants.BLUE
WHITE = constants.WHITE
BLACK = constants.WHITE
YELLOW = constants.YELLOW

WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
SPAN = constants.SPAN



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
my_dice1 = dice.FirstDie()
my_dice2 = dice.SecondDie()

# # picture
# background_img = pygame.image.load(my_board.image_loc).convert()
# background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))


all_sprites = pygame.sprite.Group()
# all_sprites.add(token1)  # TODO: how to keep transparence?
all_sprites.add(token2)
# all_sprites.add(token3)
# all_sprites.add(token4)  # TODO: how to keep transparence?
all_sprites.add(my_dice1)
all_sprites.add(my_dice2)

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
                my_dice1.roll()
                my_dice2.roll()
                dice_point = my_dice1.point + my_dice2.point
                print(f"dice point is {dice_point}.")
                token2.location(dice_point)

    





    # render
    # screen.fill(WHITE)
    screen.blit(my_board.image, (0,0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
