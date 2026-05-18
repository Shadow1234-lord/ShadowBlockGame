import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shadow Mini Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 150, 255)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(100, 100, 50, 50)
player_speed = 5
player_health = 100

# Enemy
enemy = pygame.Rect(500, 300, 50, 50)
enemy_speed = 3

# Game state
menu = True
game_over = False


def draw_text(text, x, y, color=WHITE):
    font = pygame.font.SysFont(None, 40)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


while True:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Start game from menu
        if menu and event.type == pygame.KEYDOWN:
            menu = False

        # Restart on game over
        if game_over and event.type == pygame.KEYDOWN:
            player.x, player.y = 100, 100
            player_health = 100
            game_over = False
            menu = True

    # MENU SCREEN
    if menu:
        draw_text("PRESS ANY KEY TO START", 200, 250)
        pygame.display.update()
        continue

    # GAME OVER SCREEN
    if game_over:
        draw_text("GAME OVER", 320, 250, RED)
        draw_text("PRESS ANY KEY TO RESTART", 180, 300)
        pygame.display.update()
        continue

    # MOVING CHARACTER
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Keep player within screen bounds
    if player.x < 0:
        player.x = 0
    if player.x > WIDTH - player.width:
        player.x = WIDTH - player.width
    if player.y < 0:
        player.y = 0
    if player.y > HEIGHT - player.height:
        player.y = HEIGHT - player.height

    # Enemy AI (follows player)
    if enemy.x < player.x:
        enemy.x += enemy_speed
    if enemy.x > player.x:
        enemy.x -= enemy_speed
    if enemy.y < player.y:
        enemy.y += enemy_speed
    if enemy.y > player.y:
        enemy.y -= enemy_speed

    # Keep enemy within screen bounds
    if enemy.x < 0:
        enemy.x = 0
    if enemy.x > WIDTH - enemy.width:
        enemy.x = WIDTH - enemy.width
    if enemy.y < 0:
        enemy.y = 0
    if enemy.y > HEIGHT - enemy.height:
        enemy.y = HEIGHT - enemy.height

    # COLLISION
    if player.colliderect(enemy):
        player_health -= 1

    if player_health <= 0:
        game_over = True

    # DRAW OBJECTS
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    # HEALTH BAR
    pygame.draw.rect(screen, RED, (20, 20, 200, 20))
    pygame.draw.rect(screen, BLUE, (20, 20, player_health * 2, 20))

    draw_text(f"HP: {player_health}", 20, 50)

    pygame.display.update()
