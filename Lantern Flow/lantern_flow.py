import pygame
import random


# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
LANTERN_SPEED = 2
NUDGE_AMOUNT = 3

# Colors
DARK_BLUE = (10, 10, 40)
LIGHT_BLUE = (50, 50, 100)
ORANGE = (255, 150, 50)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lantern Flow")

# Load Assets
lantern_img = pygame.image.load("lantern.png")
lantern_img = pygame.transform.scale(lantern_img, (50, 50))

# Lantern Position
lantern_x = WIDTH // 2
lantern_y = HEIGHT - 150

# Obstacles (branches)
branches = []
for _ in range(5):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(-600, -50)
    branches.append(pygame.Rect(x, y, 50, 10))

# Fireflies (bonus points)
fireflies = []
for _ in range(3):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(-600, -50)
    fireflies.append(pygame.Rect(x, y, 10, 10))

# Game Loop
running = True
score = 0
clock = pygame.time.Clock()
while running:
    screen.fill(DARK_BLUE)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        lantern_x -= NUDGE_AMOUNT
    if keys[pygame.K_RIGHT]:
        lantern_x += NUDGE_AMOUNT

    # Draw Lantern
    screen.blit(lantern_img, (lantern_x, lantern_y))

    # Move & Draw Obstacles
    for branch in branches:
        branch.y += LANTERN_SPEED
        pygame.draw.rect(screen, LIGHT_BLUE, branch)
        if branch.y > HEIGHT:
            branch.y = random.randint(-600, -50)
            branch.x = random.randint(100, WIDTH - 100)
            score += 1  # Avoiding obstacles gives points

    # Move & Draw Fireflies
    for firefly in fireflies:
        firefly.y += LANTERN_SPEED
        pygame.draw.rect(screen, ORANGE, firefly)
        if firefly.y > HEIGHT:
            firefly.y = random.randint(-600, -50)
            firefly.x = random.randint(100, WIDTH - 100)

    # Display Score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
