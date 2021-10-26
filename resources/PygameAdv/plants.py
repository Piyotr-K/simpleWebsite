import pygame
import random

# Define file path for images
IMAGE_PATH = "imgs/"
FOLDER_PATH = "./Plants/"

# Screen size constants
SCREEN_W = 800
SCREEN_H = 560

# Keep track of game state
GAMEOVER = False

# LOG string for logging errors
LOG = f"File: {__file__} Method: {__name__} Error"

# Map class to generate the map
class Map():

    map_names_list = [FOLDER_PATH + IMAGE_PATH + "map1.png", FOLDER_PATH + IMAGE_PATH + "map2.png"]

    def __init__(self, x, y, img_index):
        self.image = pygame.image.load(Map.map_names_list[img_index])
        self.position = (x, y)
        self.can_grow = True
    
    def load_map(self):
        MainGame.window.blit(self.image, self.position)

# Plants class
class Plant(pygame.sprite.Sprite):
    def __init__(self):
        super(Plant, self).__init__()
        self.live = True

    def load_image(self):
        if hasattr(self, 'image') and hasattr(self, 'rect'):
            MainGame.window.blit(self.image, self.rect)
        else:
            print(LOG)

# Sunflower class
class Sunflower(Plant):
    def __init__(self, x, y):
        super(Sunflower, self).__init__()
        self.image = pygame.image.load(FOLDER_PATH + IMAGE_PATH + "sunflower.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 50
        self.hp = 100
        # Counter to keep track of time passed
        self.time_count = 0

    # Function for money/sun production
    def produce_money(self):
        self.time_count += 1
        if self.time_count == 25:
            MainGame.money += 5
            self.time_count = 0

    # Showing the sunflower on the screen
    def display_sunflower(self):
        MainGame.window.blit(self.image, self.rect)

# Peashooter class
class Peashooter(Plant):
    def __init__(self, x, y):
        super(Peashooter, self).__init__()
        self.image = pygame.image.load(FOLDER_PATH + IMAGE_PATH + "peashooter.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 100
        self.hp = 200
        # Counter for keeping track of time since last shot
        self.shot_count = 0

    # Firing method
    def shoot(self):
        should_fire = False

        # Only shoot if a zombie is present
        for zombie in MainGame.zombie_list:
            if zombie.rect.y == self.rect.y and \
                zombie.rect.x < 800 and \
                    zombie.rect.x > self.rect.x:
                should_fire = True

        if self.live and should_fire:
            self.shot_count += 1

            if self.shot_count == 25:
                peabullet = PeaBullet(self)

                MainGame.peabullet_list.append(peabullet)
                self.shot_count = 0

    # Show the peashooter
    def display_peashooter(self):
        MainGame.window.blit(self.image, self.rect)

class PeaBullet(pygame.sprite.Sprite):
    def __init__(self, peashooter):
        self.live = True
        self.image = pygame.image.load(FOLDER_PATH + IMAGE_PATH + "peabullet.png")
        self.damage = 50
        self.speed = 10
        self.rect = self.image.get_rect()
        self.rect.x = peashooter.rect.x + 60
        self.rect.y = peashooter.rect.y + 15

    def move_bullet(self):
        if self.rect.x < SCREEN_W:
            self.rect.x += self.speed
        else:
            self.live = False
    
    def hit_zombie(self):
        for zombie in MainGame.zombie_list:
            if pygame.sprite.collide_rect(self, zombie):
                self.live = False
                zombie.hp -= self.damage
                if zombie.hp <= 0:
                    zombie.live = False
                    self.nextLevel()
    
    def nextLevel(self):
        MainGame.score += 20
        MainGame.remaining_score -= 20
        for i in range(1, 100):
            if MainGame.score == 100 * i and MainGame.remaining_score == 0:
                MainGame.remaining_score = 100 * i
                MainGame.level += 1
                MainGame.produce_zombie += 50

    def display_bullet(self):
        MainGame.window.blit(self.image, self.rect)

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Zombie, self).__init__()
        self.image = pygame.image.load(FOLDER_PATH + IMAGE_PATH + "zombie.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 1000
        self.damage = 2
        self.speed = 1
        self.live = True
        self.stop = False
    
    def move_zombie(self):
        if self.live and not self.stop:
            self.rect.x -= self.speed
            if self.rect.x < -80:
                global GAMEOVER
                GAMEOVER = True
    
    def hit_plant(self):
        for plant in MainGame.plants_list:
            if pygame.sprite.collide_rect(self, plant):
                # Zombies stop at plants to attacc
                self.stop = True
                self.eat_plant(plant)
    
    def eat_plant(self, plant):
        plant.hp -= self.damage
        if plant.hp <= 0:
            a = plant.rect.x // 80 - 1
            b = plant.rect.y // 80
            map = MainGame.map_list[a][b]
            map.can_grow = True
            plant.live = False
            self.stop = False

    def display_zombie(self):
        MainGame.window.blit(self.image, self.rect)

# Main game class
class MainGame():

    level = 1
    score = 0
    # Score required to move onto the next level
    remaining_score = 100
    money = 200

    # Store all map coordinate points
    map_points_list = []

    # Store all map tiles
    map_list = []

    # Plants list
    plants_list = []

    # Bullet list
    peabullet_list = []

    # Zombie related variables
    zombie_list = []
    count_zombie = 0
    produce_zombie = 100

    def init_window(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    
    def load_plants(self):
        for plant in MainGame.plants_list:
            if plant.live:
                if isinstance(plant, Sunflower):
                    plant.display_sunflower()
                    plant.produce_money()
                elif isinstance(plant, Peashooter):
                    plant.display_peashooter()
                    plant.shoot()
            else:
                MainGame.plants_list.remove(plant)
    
    def load_peabullets(self):
        for b in MainGame.peabullet_list:
            # If the bullet is moving through the air
            if b.live:
                b.display_bullet()
                b.move_bullet()
                b.hit_zombie()
            else:
                MainGame.peabullet_list.remove(b)

    def init_zombies(self):
        for i in range(1, 7):
            dis = random.randint(1, 5) * 200
            zombie = Zombie(800 + dis, i * 80)
            MainGame.zombie_list.append(zombie)

    def load_zombies(self):
        for zombie in MainGame.zombie_list:
            if zombie.live:
                zombie.display_zombie()
                zombie.move_zombie()
                zombie.hit_plant()
            else:
                MainGame.zombie_list.remove(zombie)

    def init_plant_points(self):
        # Create row by row
        for y in range(1, 7):
            points = []
            # Create each cell by column
            for x in range(10):
                point = (x, y)
                points.append(point)
            MainGame.map_points_list.append(points) # 2D Array
            print(f"MainGame.map_points_list{MainGame.map_points_list}")

    def init_map(self):
        # Place the tiles on the map
        for points in MainGame.map_points_list:
            temp_map_list = list()
            for point in points:
                # Alternates placing light green and dark green tiles on the map
                if (point[0] + point[1]) % 2 == 0:
                    map = Map(point[0] * 80, point[1] * 80, 0)
                else:
                    map = Map(point[0] * 80, point[1] * 80, 1)
                temp_map_list.append(map)
                # Debugging
                print(f"temp_map_list: {temp_map_list}")
            # Finalize the list
            MainGame.map_list.append(temp_map_list)
        # Debugging
        print(f"MainGame.map_list: {MainGame.map_list}")

    # Actually render all the images to the screen
    def load_map(self):
        for temp_map_list in MainGame.map_list:
            for map in temp_map_list:
                map.load_map()

    def draw_text(self, content, size, color):
        pygame.font.init()
        font = pygame.font.SysFont('kaiti', size)
        text = font.render(content, True, color)
        return text
    
    def load_help_text(self):
        text1 = self.draw_text("1. Left Click to create a sunflower 2. Right Click to create a peashooter",
                                26, (255, 0, 0))
        MainGame.window.blit(text1, (5, 5))
    
    def run_events(self):
        global GAMEOVER
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                GAMEOVER = True
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x = e.pos[0] // 80
                y = e.pos[1] // 80
                map = MainGame.map_list[y - 1][x]
                print(map.position)
                if e.button == 1:
                    if map.can_grow and MainGame.money >= 50:
                        sunflower = Sunflower(map.position[0], map.position[1])
                        MainGame.plants_list.append(sunflower)
                        print(f'Plants list length: {len(MainGame.plants_list)}')
                        map.can_grow = False
                        MainGame.money -= sunflower.price
                elif e.button == 3:
                    if map.can_grow and MainGame.money >= 100:
                        peashooter = Peashooter(map.position[0], map.position[1])
                        MainGame.plants_list.append(peashooter)
                        print(f'Plants list length: {len(MainGame.plants_list)}')
                        map.can_grow = False
                        MainGame.money -= peashooter.price
    
    def start_game(self):

        global GAMEOVER

        self.init_window()

        self.init_plant_points()
        self.init_map()

        self.init_zombies()

        while not GAMEOVER:
            MainGame.window.fill((255, 255, 255))

            MainGame.window.blit(self.draw_text(f"Sun: {MainGame.money}", 26, (255, 0, 0)), (500, 40))
            MainGame.window.blit(
                self.draw_text(
                f"Current Level: {MainGame.level}, Score: {MainGame.score}, To Next Level: {MainGame.remaining_score}",
                26,
                (255,0,0)),
                (5,40)
            )
            self.load_help_text()

            self.load_map()

            self.load_plants()

            self.load_peabullets()

            self.load_zombies()

            self.run_events()

            MainGame.count_zombie += 1
            if MainGame.count_zombie == MainGame.produce_zombie:
                self.init_zombies()
                MainGame.count_zombie = 0
            pygame.time.wait(10)

            pygame.display.update()
        
        self.gameOver()
    
    def gameOver(self):
        MainGame.window.blit(self.draw_text('Game Over', 50, (255, 0, 0)), (300, 200))
        pygame.display.update()
        pygame.time.wait(1000)


if __name__ == '__main__':
    game = MainGame()
    game.start_game()