import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, img, width, height, x, y, speed, game):
        super().__init__()
        self.game = game
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()
        self.speed = speed
        self.FRICTION = -0.1
        self.MAX_SPEED = 10

        # Animation variables
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
    
    def load_images(self):
        # Idle animation frames
        self.standing_frames = [
            self.game.spritesheet.get_image(614, 1063, 120, 191),
            self.game.spritesheet.get_image(690, 406, 120, 201)]

        # Get rid of black box for every image
        for frame in self.standing_frames:
            frame.set_colorkey(black)
        
        self.walk_frames_r = [
            self.game.spritesheet.get_image(678, 860, 120, 201),
            self.game.spritesheet.get_image(692, 1458, 120, 207)]
        self.walk_frames_l = []

        for frame in self.walk_frames_r:
            frame.set_colorkey(black)
            self.walk_frames_l.append(pygame.transform.flip(frame, True, False))
        
        # Jump Frame
        self.jump_frame = self.game.spritesheet.get_image(382, 763, 150, 181)
        self.jump_frame.set_colorkey(black)
    
    def animate(self):
        now = pygame.time.get_ticks()

        self.jumping = self.velocity.y != 0
        if self.jumping:
            self.last_update = now
            bottom = self.rect.bottom
            x = self.rect.x
            self.image = self.jump_frame
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.x = x

        self.walking = self.velocity.x != 0
        if self.walking:
            if now - self.last_update > 180:
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                x = self.rect.x
                if self.velocity.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.x = x

        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(self.standing_frames)
                x = self.rect.x
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.x = x
        
    
    def update(self):
        self.animate()
        pressed_keys = pygame.key.get_pressed()
        self.acceleration.update(0, 0.5)
        if pressed_keys[pygame.K_LEFT]:
            self.acceleration.x += -1
        if pressed_keys[pygame.K_RIGHT]:
            self.acceleration.x += 1
        
        self.acceleration *= self.speed
        self.acceleration.x += self.velocity.x * self.FRICTION
        self.velocity += self.acceleration

        if abs(self.velocity.x) < 1:
            self.velocity.x = 0

        if abs(self.velocity.x) > self.MAX_SPEED:
            if self.velocity.x < 0:
                self.velocity.x = -self.MAX_SPEED
            else:
                self.velocity.x = self.MAX_SPEED

        self.rect.move_ip(self.velocity + 0.5 * self.acceleration)

        if self.rect.right <= 0:
            self.rect.right = screen_w
        elif self.rect.left > screen_w:
            self.rect.left = 0
    
    def jump(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2
        if hits:
            self.velocity.y = -20
            self.game.jump_sound.play()
    
    def jump_cut(self):
        if self.jumping and self.velocity.y < -3:
            self.velocity.y = -3

class Mob(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.mobs
        super().__init__(self.groups)
        self.game = game
        self.image_up = self.game.spritesheet.get_image(566, 510, 122, 139)
        self.image_up.set_colorkey(black)
        self.image_down = self.game.spritesheet.get_image(568, 1534, 122, 135)
        self.image_down.set_colorkey(black)
        self.image = self.image_up
        self.rect = self.image.get_rect()
        # Spawn the enemy from either the left side of the screen
        # or the right
        self.rect.centerx = random.choice([-100, screen_w + 100])
        self.vx = random.randrange(1, 4)
        if self.rect.centerx > screen_w:
            self.vx *= -1
        # Spawn the enemy in the top half of the screen somewhere
        self.rect.y = random.randrange(screen_h / 2)
        self.vy = 0
        self.dy = 0.5
    
    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        # Reverse the y direction if the enemy bobs past 3 in the y axis
        if self.vy > 3 or self.vy < -3:
            self.dy *= -1
        center = self.rect.center
        # "Animate" the sprite by cycling the image between up and down
        if self.dy < 0:
            self.image = self.image_up
        else:
            self.image = self.image_down
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.y += self.vy
        # If the enemy leaves the right or left side of the screen
        # delete the sprite
        if self.rect.left > screen_w + 100 or self.rect.right < -100:
            self.kill()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.groups = game.all_sprites, game.platforms
        super().__init__(self.groups)
        self.game = game
        images = [self.game.spritesheet.get_image(0, 288, 380, 94),
                    self.game.spritesheet.get_image(213, 1662, 201, 100)]
        self.image = random.choice(images)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if random.randrange(100) < 15:
            Pow(self.game, self)

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()
    
    def get_image(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.spritesheet, (0,0), (x, y, w, h))
        image = pygame.transform.scale(image, (w // 2, h // 2))
        return image

class Pow(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self.groups = game.all_sprites, game.powerups
        super().__init__(self.groups)
        self.game = game
        self.plat = plat
        self.type = random.choice(['boost'])
        self.image = self.game.spritesheet.get_image(820, 1805, 71, 70)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()