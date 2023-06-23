import os
import pygame
import constants
import random

WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
DIE_WIDTH = WIDTH * 0.2
DIE_HEIGHT = DIE_WIDTH

class FirstDie(pygame.sprite.Sprite):  # TODO: make these two die herit from single class
    def __init__(self, name="classic"):
        super().__init__()
        self.name = name
        self.point = 6  # initiate
        # set image size and location
        self.image_loc = os.path.join("pic", r"die_" + self.name + r"_" + str(self.point) + r".png")
        self.image = pygame.image.load(self.image_loc).convert()
        self.image = pygame.transform.scale(self.image, (DIE_WIDTH, DIE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH * 0.5 - DIE_WIDTH * 0.55
        self.rect.centery = HEIGHT * 0.5

    def roll(self):
        random.seed()
        self.point = random.randint(1, 6)

        # set image size and location
        self.image_loc = os.path.join("pic", r"die_" + self.name + r"_" + str(self.point) + r".png")
        self.image = pygame.image.load(self.image_loc).convert()
        self.image = pygame.transform.scale(self.image, (DIE_WIDTH, DIE_HEIGHT))


class SecondDie(FirstDie):  # inherit from FirstDie
    def __init__(self, name="classic"):
        super().__init__()
        # self.name = name
        # self.point = 6  # initiate
        # set image size and location
        # self.image_loc = os.path.join("pic", r"die_" + self.name + r"_" + str(self.point) + r".png")
        # self.image = pygame.image.load(self.image_loc).convert()
        # self.image = pygame.transform.scale(self.image, (DIE_WIDTH, DIE_HEIGHT))
        # self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH * 0.5 + DIE_WIDTH * 0.55
        # self.rect.centery = HEIGHT * 0.5

    def roll(self):
        random.seed()
        self.point = random.randint(1, 6)

        # set image size and location
        self.image_loc = os.path.join("pic", r"die_" + self.name + r"_" + str(self.point) + r".png")
        self.image = pygame.image.load(self.image_loc).convert()
        self.image = pygame.transform.scale(self.image, (DIE_WIDTH, DIE_HEIGHT))


if __name__ == "__main__":
    my_firstdie = FirstDie()
    my_firstdie.roll()
    my_seconddie = SecondDie()
    my_seconddie.roll()
    print(f"die1: {my_firstdie.point}")
    print(f"die2: {my_seconddie.point}")
    print(f"die: {my_firstdie.point + my_seconddie.point}")
    print(f"is double: {my_firstdie.point==my_seconddie.point}")
