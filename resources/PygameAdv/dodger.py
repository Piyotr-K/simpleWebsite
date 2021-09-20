import pygame, random, sys
from pygame import draw
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

def waitForKeyPress():
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                terminate()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    terminate()
                return

# Detect collision with enemy
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y, alignment=""):
    textObj = font.render(text, 1, (255,255,255))
    textrect = textObj.get_rect()
    if alignment.lower() == "center":
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    surface.blit(textObj, textrect)

# Set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
# Hides mouse when mouse is over the game
pygame.mouse.set_visible(False)

pygame.font.init()
myFont = pygame.font.SysFont('Comic Sans MS', 30)

playerImg = pygame.image.load('./dodger/player.png')
playerImg.set_colorkey((255, 255, 255))
playerRect = playerImg.get_rect()

baddieImage = pygame.image.load('./dodger/baddie.png')

topScore = 0

# show the "Start" Screen
drawText('Dodger', myFont, windowSurface,
        (WINDOWWIDTH // 2), (WINDOWHEIGHT // 2), "center")
drawText('Press any key to start the game', myFont, windowSurface,
        (WINDOWWIDTH // 2), (WINDOWHEIGHT // 2) + 100, "center")
pygame.display.update()
waitForKeyPress()

# Outside replay loop
while True:

    # Set player position
    playerRect.topleft = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2)

    # List to keep track of all the enemies
    baddies = []

    # Counter to keep track of how long its been since the last enemy was added
    baddieAddCounter = 0

    # Current score
    score = 0

    # Booleans to keep track of player movement
    moveLeft = moveRight = moveUp = moveDown = False

    while True:

        # For every frame we survive we get 1 point
        score += 1
        
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
            if score >= 300 and score < 500:
                ADDNEWBADDIERATE = 9
            elif score >= 500 and score < 700:
                ADDNEWBADDIERATE = 8
            elif score >= 700 and score < 1000:
                ADDNEWBADDIERATE = 7
            elif score >= 1000 and score < 1200:
                ADDNEWBADDIERATE = 6
            elif score >= 1200 and score < 1600:
                ADDNEWBADDIERATE = 5
            elif score >= 1600 and score < 2000:
                ADDNEWBADDIERATE = 4
            elif score >= 2000 and score < 2500:
                ADDNEWBADDIERATE = 3
            elif score >= 2500:
                ADDNEWBADDIERATE = 1
            elif score <= 300:
                ADDNEWBADDIERATE = 10
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize,
                                            baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }
            
            baddies.append(newBaddie)
        
        # Draw the baddies
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        # Move the baddies down
        for b in baddies:
            b['rect'].move_ip(0, b['speed'])

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        drawText(f'Score: {score}', myFont, windowSurface, 1, 0)
        drawText(f'Top Score: {topScore}', myFont, windowSurface, 1, 30)
        
        # Lock the game to a certain frame rate
        mainClock.tick(FPS)

        pygame.display.update()

        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score
            break