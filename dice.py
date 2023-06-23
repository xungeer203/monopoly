import os
import pygame
import constants
import random

WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT
DIE_WIDTH = WIDTH * 0.2
DIE_HEIGHT = DIE_WIDTH

# class TwoDice:
#     """This class is to simulate rolling two dice, and to get points.
#     """
#     def __init__(self):
#         self.point1 = 0
#         self.point2 = 0
#         self.point = 0
#         self.is_double = False

#     def roll(self):
#         random.seed()
#         self.point1 = random.randint(1, 6)
#         self.point2 = random.randint(1, 6)
#         self.point = self.point1 + self.point2
#         self.is_double = True if self.point1 == self.point2 else False


# class FirstDice(pygame.sprite.Sprite):
#     def __init__(self, name="classic"):
#         super().__init__()
#         self.name = name
#         self.point1 = 0
#         self.point2 = 0
#         self.point = 0
#         self.is_double = False

#     def roll(self):
#         random.seed()
#         self.point1 = random.randint(1, 6)
#         self.point2 = random.randint(1, 6)
#         self.point = self.point1 + self.point2
#         self.is_double = True if self.point1 == self.point2 else False

#         # set image size and location
#         self.image1_loc = os.path.join("pic", r"die_" + self.name + r"_" + self.point1 + r".png")
#         self.image1 = pygame.image.load(self.image_loc1).convert()
#         self.image1 = pygame.transform.scale(self.image1, (200, 200))
#         self.rect1 = self.image1.get_rect()
#         self.rect1.centerx = WIDTH * 0.5 - 100
#         self.rect1.centery = HEIGHT

#         self.image2_loc = os.path.join("pic", r"die_" + self.name + r"_" + self.point2 + r".png")
#         self.image2 = pygame.image.load(self.image_loc2).convert()
#         self.image2 = pygame.transform.scale(self.image2, (200, 200))
#         self.rect2 = self.image2.get_rect()
#         self.rect2.centerx = WIDTH * 0.5 + 100
#         self.rect2.centery = HEIGHT

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
    my_twodice = TwoDice()  # TODO: to be modified
    my_twodice.roll()
    print(f"die1: {my_twodice.point1}")
    print(f"die2: {my_twodice.point2}")
    print(f"die: {my_twodice.point}")
    print(f"is double: {my_twodice.is_double}")
