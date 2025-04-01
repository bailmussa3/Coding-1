

# Initialize Pygame
pygame.init()

# Set up display
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Moving Game Object')

# Set up clock for FPS control
clock = pygame.time.Clock()

# Load the image for the object
playerImg = pygame.image.load('player_image.png')  # Replace 'player_image.png' with your image path

# Get the size of the image
player_width = playerImg.get_width()
player_height = playerImg.get_height()

# Initial position of the object
x = display_width // 2 - player_width // 2
y = display_height // 2 - player_height // 2
speed = 5  # Speed of movement

# Function to display the image at the current position
def player(x, y):
    gameDisplay.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of the keys to move the object
    keys = pygame.key.get_pressed()

    # Moving the player
    if keys[pygame.K_LEFT]:
        x -= speed  # Move left
    if keys[pygame.K_RIGHT]:
        x += speed  # Move right
    if keys[pygame.K_UP]:
        y -= speed  # Move up
    if keys[pygame.K_DOWN]:
        y += speed  # Move down

    # Ensure the player doesn't move out of bounds
    if x < 0:
        x = 0
    if x > display_width - player_width:
        x = display_width - player_width
    if y < 0:
        y = 0
    if y > display_height - player_height:
        y = display_height - player_height

    # Fill the screen with a white color
    gameDisplay.fill((255, 255, 255))

    # Draw the player image at the new position
    player(x, y)

    # Update the display
    pygame.display.update()

    # Set FPS (frames per second)
    clock.tick(60)

# Quit Pygame
pygame.quit()










import pygame
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

# Function to draw basketball
def draw_ball(x, y):
    pygame.draw.circle(screen, RED, (x, y), ball_radius)

# Function to draw hoop
def draw_hoop():
    pygame.draw.rect(screen, GREEN, (hoop_x, hoop_y, hoop_width, hoop_height))

# Function to draw score
def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Ball movement control
    if keys[pygame.K_LEFT]:
        ball_x -= 5
    if keys[pygame.K_RIGHT]:
        ball_x += 5
    if keys[pygame.K_DOWN]:
        ball_y += 5
    if keys[pygame.K_UP] and ball_y == SCREEN_HEIGHT - 150:  # Only jump when on the ground
        ball_speed_y = -15  # Jump velocity
    
    # Apply gravity to the ball
    ball_speed_y += gravity
    ball_y += ball_speed_y

    # Ball collision with the ground
    if ball_y >= SCREEN_HEIGHT - 150:
        ball_y = SCREEN_HEIGHT - 150
        ball_speed_y = 0

    # Check if the ball is in the hoop
    if (hoop_x < ball_x < hoop_x + hoop_width) and (hoop_y < ball_y < hoop_y + hoop_height):
        score += 1  # Increment score
        ball_x = 100  # Reset ball position
        ball_y = SCREEN_HEIGHT - 150
        ball_speed_y = 0

    # Draw the basketball hoop and ball
    draw_hoop()
    draw_ball(ball_x, ball_y)
    draw_score()

    # Update the screen
    pygame.display.update()

    # Set game frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
