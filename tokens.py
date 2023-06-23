"""this file to make tokens for players, such as dinosaur, hat, dog, ...
"""

import os
import pygame
import constants

# SPAN = 1080 / 12.2  
SPAN = constants.SPAN
WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
OFFSET_X = 0
OFFSET_Y = 0

class Token(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name

        # set image size and location
        self.image_loc = os.path.join("pic", r"token_" + name + r".png")
        self.image = pygame.image.load(self.image_loc).convert()
        self.image = pygame.transform.scale(self.image, (72, 72))
        self.rect = self.image.get_rect()

        # initial position
        self.steps = 20  # "steps" will increase along with dice points
        self.location(0)
        
        self.money = 0

    def location(self, dice_point):
        self.steps += dice_point
        steps_dummy = self.steps % 40  # 40 steps in total in single loop

        if steps_dummy in range(0,10):
            cell_x = steps_dummy
            cell_y = 0
        elif steps_dummy in range(10, 20):
            cell_x = 10
            cell_y = (steps_dummy - 10)
        elif steps_dummy in range(20, 30):
            cell_x = (30 - steps_dummy)
            cell_y = 10
        elif steps_dummy in range(30, 40):
            cell_x = 0
            cell_y = (40 - steps_dummy)
        else:
            cell_x = 5  # if error, place the token in the middle of board.
            cell_y = 5

        self.rect.centerx = cell_x * SPAN + SPAN
        self.rect.centery = cell_y * SPAN + SPAN * 0.8


if __name__ == "__main__":
    play1_token = Token("tophat")
    play2_token = Token("boot")
    play3_token = Token("racecar")
    play4_token = Token("battleship")
    print (f"Player 4 is {play4_token.image_loc}")
