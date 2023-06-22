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

        self.steps = 0  # "steps" will increase along with dice points; initial steps is 20, because the start point is right bottom of the board.

        # set image size and location
        # self.image_loc = r"pic\token_" + name + r".png"
        self.image_loc = os.path.join("pic", r"token_" + name + r".png")
        self.image = pygame.image.load(self.image_loc).convert()
        self.image = pygame.transform.scale(self.image, (79, 79))
        # self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 980/1080 * WIDTH
        self.rect.centery = 1000/1080 * HEIGHT

        
        self.money = 0
        self.position = (0, 0)

    def location(self, dice_point):
        print("before rolling dice, step: {}".format(self.steps))
        self.steps += dice_point
        print("after rolling dice, step: {}".format(self.steps))
        steps_dummpy = self.steps % 40  # 40 steps in total in single loop
        print("steps_dummy:{}".format(steps_dummpy))

        # print("before rolling dice, centerx: {}".format(self.rect.centerx))
        # print("before rolling dice, centery: {}".format(self.rect.centery))

        # TODO: to be continued next time: the first rolling dice is incorrect.
        if steps_dummpy in range(0,10):
            self.rect.centerx = steps_dummpy
            self.rect.centery = 0
        elif steps_dummpy in range(10, 20):
            self.rect.centerx = 10
            self.rect.centery = (steps_dummpy - 10)
        elif steps_dummpy in range(20, 30):
            self.rect.centerx = (30 - steps_dummpy)
            self.rect.centery = 10
        elif steps_dummpy in range(30, 40):
            self.rect.centerx = 0
            self.rect.centery = (40 - steps_dummpy)
        else:
            self.rect.centerx = 5  # if error, place the token in the middle of board.
            self.rect.centery = 5

        self.rect.centerx *= SPAN
        self.rect.centery *= SPAN


if __name__ == "__main__":
    play1_token = Token("tophat")
    play2_token = Token("boot")
    play3_token = Token("racecar")
    play4_token = Token("battleship")
    print (f"Player 4 is {play4_token.image_loc}")
