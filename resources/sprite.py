import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, img, width, height, x, y, speed, game):
        super().__init__()
        self.image = pygame.image.load(f"{folder}/{img}")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()
        self.speed = speed
        self.FRICTION = -0.1
        self.MAX_SPEED = 10
        self.game = game
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        self.acceleration.update(0, 0.5)
        if pressed_keys[pygame.K_LEFT]:
            self.acceleration.x += -1
        if pressed_keys[pygame.K_RIGHT]:
            self.acceleration.x += 1
        
        self.acceleration *= self.speed
        self.acceleration.x += self.velocity.x * self.FRICTION
        self.velocity += self.acceleration

        if abs(self.velocity.x) > self.MAX_SPEED:
            if self.velocity.x < 0:
                self.velocity.x = -self.MAX_SPEED
            else:
                self.velocity.x = self.MAX_SPEED

        self.rect.move_ip(self.velocity + 0.5 * self.acceleration)

        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocity.x = 0
        elif self.rect.right > screen_w:
            self.rect.right = screen_w
            self.velocity.x = 0
    
    def jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits:
            self.velocity.y = -15


class Platform(pygame.sprite.Sprite):
    def __init__(self, w, h, x, y, color):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image.fill(color)