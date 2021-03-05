from settings import *
from colors import *
from sprite import *

class Game:
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
    
    def draw(self):
        self.screen.fill(white)
        self.all_sprites.draw(self.screen)
        pygame.display.update()
    
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
        ground = Platform(screen_w, 50, 0, screen_h - 50, red)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        p1 = Platform(200, 20, 100, screen_h - 150, red)
        self.all_sprites.add(p1)
        self.platforms.add(p1)

game = Game()
game.level_1()
game.run()