import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
PLAYERMOVERATE = 5
FPS = 30
BACKGROUNDCOLOR = (0, 0, 0)

# El bad guy variables
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 30
BADDIEMINSPEED = 5
BADDIEMAXSPEED = 15
ADDNEWBADDIERATE = 10

def terminate():
    pygame.quit()
    sys.exit()

# Set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
# Hides mouse when mouse is over the game
pygame.mouse.set_visible(False)

playerImg = pygame.image.load('./dodger/player.png')
playerImg.set_colorkey((255, 255, 255))
playerRect = playerImg.get_rect()

baddieImage = pygame.image.load('./dodger/baddie.png')

# Outside replay loop
while True:

    # Set player position
    playerRect.topleft = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2)

    # List to keep track of all the enemies
    baddies = []

    # Counter to keep track of how long its been since the last enemy was added
    baddieAddCounter = 0

    # Booleans to keep track of player movement
    moveLeft = moveRight = moveUp = moveDown = False

    while True:
        
        # Paint the background colour every tick
        windowSurface.fill(BACKGROUNDCOLOR)

        # Render the player image
        windowSurface.blit(playerImg, playerRect)

        for e in pygame.event.get():
            if e.type == QUIT:
                terminate()
            
            if e.type == KEYDOWN:
                if e.key == K_UP or e.key == ord('w'):
                    moveUp = True
                    moveDown = False
                if e.key == K_LEFT or e.key == ord('a'):
                    moveLeft = True
                    moveRight = False
                if e.key == K_DOWN or e.key == ord('s'):
                    moveUp = False
                    moveDown = True
                if e.key == K_RIGHT or e.key == ord('d'):
                    moveRight = True
                    moveLeft = False
            
            if e.type == KEYUP:
                if e.key == K_ESCAPE:
                    terminate()
                if e.key == K_UP or e.key == ord('w'):
                    moveUp = False
                if e.key == K_LEFT or e.key == ord('a'):
                    moveLeft = False
                if e.key == K_DOWN or e.key == ord('s'):
                    moveDown = False
                if e.key == K_RIGHT or e.key == ord('d'):
                    moveRight = False
            
            if e.type == MOUSEMOTION:
                # If the mouse moves, move the player where the cursor is
                playerRect.move_ip(e.pos[0] - playerRect.centerx,
                                    e.pos[1] - playerRect.centery)
        
        baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize,
                                            baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)
        
        # Lock the game to a certain frame rate
        mainClock.tick(FPS)

        pygame.display.update()