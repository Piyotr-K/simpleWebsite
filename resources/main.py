from settings import *
from colors import *
from sprite import *
import random

class Game:

    score = 0
    font_name = pygame.font.match_font('Arial')
    # Exact path = "C:/Windows/Fonts/Arial.ttf"
    # For Mac
    # font_name = "~/Library/Fonts/times.ttf"

    def __init__(self):
        self.screen = pygame.display.set_mode((screen_w, screen_h))
        self.clock = pygame.time.Clock()
        self.playing = True

        self.pikachu = Player("pikachu.png", 50, 50,
                            screen_w // 2, screen_h // 2, 1.5, self)
        
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.reset()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pikachu.jump()
    
    def update(self):
        self.all_sprites.update()
        if self.pikachu.velocity.y > 0:
            hits = pygame.sprite.spritecollide(self.pikachu, self.platforms, False)
            if hits:
                self.pikachu.rect.bottom = hits[0].rect.top
                self.pikachu.velocity.y = 0
        
        # Scrolling platforms downwards
        if self.pikachu.rect.top <= screen_h / 4:
            self.pikachu.rect.y += abs(self.pikachu.velocity.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.pikachu.velocity.y)
                if plat.rect.top >= screen_h:
                    plat.kill()
                    self.score += 1
        
        # Falling
        if self.pikachu.rect.bottom > screen_h:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.pikachu.velocity.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        
        # End game
        if len(self.platforms) == 0:
            self.playing = False
        
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(width, 20,
                        random.randrange(0, screen_w - width),
                        random.randrange(-75, -30),
                        red)
            self.platforms.add(p)
            self.all_sprites.add(p)
    
    def draw(self):
        self.screen.fill(white)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, black, screen_w / 2, 15)
        pygame.display.update()
    
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def run(self):
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()
    
    def reset(self):
        self.all_sprites.empty()
        self.all_sprites.add(self.pikachu)
    
    def level_1(self):
        self.reset()
        platform_list = [
            (screen_w, 50, 0, screen_h - 50, red),
            (100, 20, screen_w / 2 - 50, screen_h * 3 / 4, red),
            (100, 20, 125, screen_h - 250, red),
            (100, 20, 350, 200, red),
            (50, 20, 175, 150, red)
        ]
        for plat in platform_list:
            w, h, x, y, color = plat
            p = Platform(w, h, x, y, color)
            self.all_sprites.add(p)
            self.platforms.add(p)

game = Game()
game.level_1()
game.run()