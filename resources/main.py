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
        self.running = True

        self.load_data()
        self.pikachu = Player("pikachu.png", 50, 50,
                            screen_w // 2, screen_h // 2, 1.5, self)
        
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.reset()
    
    def load_data(self):
        try:
            with open(folder + "/highscore.txt", 'r') as f:
                try:
                    self.highscore = int(f.read())
                except:
                    self.highscore = 0
        except:
            with open(folder + "/highscore.txt", 'w') as f:
                self.highscore = 0
        self.spritesheet = Spritesheet(folder + "/spritesheet_jumper.png")
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pikachu.jump()
    
    def update(self):
        self.all_sprites.update()
        if self.pikachu.velocity.y > 0:
            hits = pygame.sprite.spritecollide(self.pikachu, self.platforms, False)
            if hits:
                if self.pikachu.rect.bottom < hits[0].rect.centery:
                    self.pikachu.rect.bottom = hits[0].rect.top
                    self.pikachu.velocity.y = 0
        
        # Scrolling platforms downwards
        if self.pikachu.rect.top <= screen_h / 4:
            self.pikachu.rect.y += max(2, abs(self.pikachu.velocity.y))
            for plat in self.platforms:
                plat.rect.y += max(2, abs(self.pikachu.velocity.y))
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
            p = Platform(random.randrange(0, screen_w - width),
                        random.randrange(-75, -30),
                        self)
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
    
    def show_gameover_screen(self):
        if not self.running:
            return
        self.screen.fill(white)
        self.draw_text("GAME OVER", 48, black, screen_w / 2, screen_h / 4)
        self.draw_text("Score: " + str(self.score), 22,
                        black, screen_w / 2, screen_h / 2)
        self.draw_text("Press a key to play again!", 22,
                        black, screen_w / 2, screen_h * 3 / 4)
        
        # Saving the highscore
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, black,
                            screen_w / 2, screen_h / 2 + 40)
            with open(folder + "/highscore.txt", 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High score: " + str(self.highscore),
                            22, black, screen_w / 2, screen_h / 2 + 40)

        pygame.display.update()
        self.wait_for_key()

    def show_main_menu(self):
        if not self.running:
            return
        self.screen.fill(white)
        self.draw_text("Doodle Jump Ripoff", 48, 
                        black, screen_w / 2, screen_h / 4)
        self.draw_text("Press a key to play!", 22,
                        black, screen_w / 2, screen_h * 3 / 4)
        pygame.display.update()
        self.wait_for_key()
   
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def reset(self):
        self.score = 0
        self.all_sprites.empty()
        self.platforms.empty()
        self.all_sprites.add(self.pikachu)
        self.pikachu.rect.x = screen_w // 2
        self.pikachu.rect.y = screen_h // 2
        self.pikachu.velocity.y = 0
    
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
            p = Platform(x, y, game)
            self.all_sprites.add(p)
            self.platforms.add(p)

game = Game()

game.show_main_menu()
while game.running:
    game.level_1()
    game.run()
    game.show_gameover_screen()