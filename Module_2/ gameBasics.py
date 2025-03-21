

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
