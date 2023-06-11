import pygame
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

WIDTH = 500
HEIGHT = 600


my_board = board.Board("blank")


# initiation and windows
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly")
clock = pygame.time.Clock()

# picture
background_img = pygame.image.load(my_board.image_loc).convert()
# rock_img = pygame.image.load(os.path.join("ref", "img", "rock.png")).convert()



# game loop
running = True
while running:
    clock.tick(FPS)  # set max. FPS. From loop view, it means this loop will be excuted 60(FPS) times per second.
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if buttd   om "close" in click
            running = False
 

    





    # render
    screen.fill(BLACK)
    screen.blit(background_img, (0,0))
    pygame.display.update()

pygame.quit()
