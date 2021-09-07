import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600

def terminate():
    pygame.quit()
    sys.exit()

# Set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
# Hides mouse when mouse over game
pygame.mouse.set_visible(False)

playerImg = pygame.image.load('./dodger/player.png')
playerRect = playerImg.get_rect()

# Outside replay loop
while True:
    playerRect.topleft = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2)

    while True:
        windowSurface.blit(playerImg, playerRect)

        for e in pygame.event.get():
            if e.type == QUIT:
                terminate()
        pygame.display.update()