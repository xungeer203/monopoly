"""this file to make tokens for players, such as dinosaur, hat, dog, ...
"""

import os
import pygame

class Token(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name

        # set image size and location
        # self.image_loc = r"pic\token_" + name + r".png"
        self.image_loc = os.path.join("pic", r"token_" + name + r".png")
        self.image = pygame.image.load(self.image_loc).convert()
        self.image = pygame.transform.scale(self.image, (79, 79))
        # self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 980    # TODO: 500 should be imported from "main.py"
        self.rect.centery = 1000

        
        self.money = 0
        self.position = (0, 0)


if __name__ == "__main__":
    play1_token = Token("tophat")
    play2_token = Token("boot")
    play3_token = Token("racecar")
    play4_token = Token("battleship")
    print (f"Player 4 is {play4_token.image_loc}")
