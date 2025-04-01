
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basketball Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Basketball properties
ball_radius = 15
ball_x = 100
ball_y = SCREEN_HEIGHT - 150
ball_speed_x = 0
ball_speed_y = 0
gravity = 0.5

# Hoop properties
hoop_width = 100
hoop_height = 10
hoop_x = SCREEN_WIDTH - hoop_width - 50
hoop_y = SCREEN_HEIGHT // 2 - 50

# Game clock
clock = pygame.time.Clock()

# Score variables
score = 0
font = pygame.font.SysFont("Arial", 24)

