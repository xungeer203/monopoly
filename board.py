"""this file to make paly board.
"""
import pygame
import constants

WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT

class Board:
    def __init__(self, name):
        import os
        self.name = name
        self.image_loc = os.path.join("pic", r"board_" + name + r".png")
        self.image = pygame.image.load(self.image_loc).convert()
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))