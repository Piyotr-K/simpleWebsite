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

# Map class to generate the map
class Map():

    map_names_list = [FOLDER_PATH + IMAGE_PATH + "map1.png", FOLDER_PATH + IMAGE_PATH + "map2.png"]

    def __init__(self, x, y, img_index):
        self.image = pygame.image.load(Map.map_names_list[img_index])
        self.position = (x, y)
        self.can_grow = True
    
    def load_map(self):
        MainGame.window.blit(self.image, self.position)

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

    def init_window(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    
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
    
    def start_game(self):

        global GAMEOVER

        self.init_window()

        self.init_plant_points()
        self.init_map()

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

            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    GAMEOVER = True
            pygame.display.update()

if __name__ == '__main__':
    game = MainGame()
    game.start_game()