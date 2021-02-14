import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, img, width, height, x, y, speed):
        super().__init__()
        self.image = pygame.image.load(f"{folder}/{img}")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = pygame.math.Vector2()
        self.speed = speed
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        self.velocity.update(0, 0)
        if pressed_keys[pygame.K_LEFT]:
            self.velocity.x += -1
        if pressed_keys[pygame.K_RIGHT]:
            self.velocity.x += 1
        self.rect.move_ip(self.velocity * self.speed)

        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocity.update(0)
        elif self.rect.right > screen_w:
            self.rect.right = screen_w
            self.velocity.update(0)