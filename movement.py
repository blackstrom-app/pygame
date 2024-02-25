import pygame
import sys


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Detection Example")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_height // 2
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)


enemy_width = 50
enemy_height = 50
enemy_x = 100
enemy_y = 100
enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    
    if player_rect.colliderect(enemy_rect):
        print("Collision detected!")

    # Fill the screen
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    
    pygame.display.flip()


    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()
