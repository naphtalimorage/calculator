import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aviator Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
plane_img = pygame.image.load('plane.png')
plane_rect = plane_img.get_rect()
plane_rect.center = (100, screen_height // 2)

coin_img = pygame.image.load('coin.png')

# Load sounds
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # Play background music indefinitely

# Game variables
player_y_change = 0
score = 0
coins = []
obstacles = []
game_over = False

# Define functions
def spawn_coin():
    x = screen_width
    y = random.randint(50, screen_height - 50)
    return pygame.Rect(x, y, 30, 30)

def spawn_obstacle():
    x = screen_width
    y = random.randint(50, screen_height - 50)
    obstacle_rect = pygame.Rect(x, y, 50, 50)
    return obstacle_rect

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    if not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_y_change = -5
                elif event.key == pygame.K_DOWN:
                    player_y_change = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_y_change = 0

        # Move the player
        plane_rect.y += player_y_change

        # Draw the player
        screen.blit(plane_img, plane_rect)

        # Spawn coins
        if random.randint(0, 100) < 2:
            coins.append(spawn_coin())

        # Spawn obstacles
        if random.randint(0, 100) < 1:
            obstacles.append(spawn_obstacle())

        # Move and draw coins
        for coin in coins:
            coin.x -= 5
            pygame.draw.rect(screen, WHITE, coin)
            screen.blit(coin_img, coin)

            # Collision detection with coins
            if coin.colliderect(plane_rect):
                score += 1
                coins.remove(coin)

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle.x -= 5
            pygame.draw.rect(screen, (255, 0, 0), obstacle)

            # Collision detection with obstacles
            if obstacle.colliderect(plane_rect):
                game_over = True

        # Draw score
        draw_text(f"Score: {score}", pygame.font.Font(None, 36), WHITE, screen_width // 2, 10)
    else:
        # Game over screen
        draw_text("GAME OVER", pygame.font.Font(None, 72), WHITE, screen_width // 2, screen_height // 2 - 50)
        draw_text(f"Score: {score}", pygame.font.Font(None, 36), WHITE, screen_width // 2, screen_height // 2 + 50)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
