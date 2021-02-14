import pygame
import os
from colors import *

# Init clock
clock = pygame.time.Clock()
fps = 60

# Initialize pygame
pygame.init()

# Setup an 800x600 game window
screen_w = 800
screen_h = 600
screen = pygame.display.set_mode((screen_w, screen_h))

# Load images
folder = os.path.dirname(__file__)