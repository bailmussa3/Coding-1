 import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 500, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
BALL_RADIUS = 10
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
HOOP_WIDTH, HOOP_HEIGHT = 100, 20

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basketball Shooting Game")

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - PLAYER_HEIGHT - 10
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

class Basketball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - PLAYER_HEIGHT - BALL_RADIUS - 10
        self.radius = BALL_RADIUS
        self.speed_x = 0
        self.speed_y = 0
        self.is_shooting = False

    def move(self):
        if self.is_shooting:
            self.x += self.speed_x
            self.y += self.speed_y
            # Gravity effect (ball falls)
            self.speed_y += 0.2
            if self.y >= HEIGHT - BALL_RADIUS:  # Ball hits the ground
                self.reset()

    def shoot(self, angle, power):
        self.is_shooting = True
        self.speed_x = power * pygame.math.cos(angle)
        self.speed_y = -power * pygame.math.sin(angle)

    def reset(self):
        self.is_shooting = False
        self.x = WIDTH // 2
        self.y = HEIGHT - PLAYER_HEIGHT - BALL_RADIUS - 10

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

class Hoop:
    def __init__(self):
        self.x = WIDTH // 2 - HOOP_WIDTH // 2
        self.y = 50
        self.width = HOOP_WIDTH
        self.height = HOOP_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

# Game loop
player = Player()
ball = Basketball()
hoop = Hoop()
score = 0
running = True

while running:
    clock.tick(FPS)
    screen.fill(WHITE)  # Clear screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Shoot the basketball when space is pressed
            if event.key == pygame.K_SPACE and not ball.is_shooting:
                # Angle and power for shooting
                angle = random.uniform(0.1, 0.3)  # Random angle for simplicity
                power = random.randint(10, 15)  # Random power for simplicity
                ball.shoot(angle, power)

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw()

    # Update and draw basketball
    ball.move()
    ball.draw()

    # Update and draw hoop
    hoop.draw()

    # Check if the ball goes through the hoop
    if hoop.x < ball.x < hoop.x + hoop.width and hoop.y < ball.y < hoop.y + HOOP_HEIGHT:
        score += 1
        ball.reset()  # Reset ball after scoring

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()  # Refresh screen

#handles events 
for event in pygame.event.get():
    if event. type == pygame.Ouit:
        running = False
        if event.key == pygame.keydown:     

pygame.quit()