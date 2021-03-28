import pygame
import colors

pygame.init()

screen = pygame.display.set_mode((800, 800))

image = pygame.image.load("pikachu.png")
image_rect = image.get_rect()
image_rect.center = (400, 400)

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False
    
    screen.fill(white)
    screen.blit(image, image_rect)