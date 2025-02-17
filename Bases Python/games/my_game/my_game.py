import random

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Set title and icon
pygame.display.set_caption('Space Invaders')

icon = pygame.image.load('space-man.png')
pygame.display.set_icon(icon)

#Player
player_img = pygame.image.load('spaceship.png')
player_x = 368
player_y = 536

player_change_x = 0
player_change_y = 0

#Enemies
enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0 ,736)
enemy_y = 0
enemy_change_x = 0.1

def update_player(x, y):
    screen.blit(player_img, (x, y))

def update_enemy(x, y):
    screen.blit(enemy_img, (x, y))

is_executing = True

while is_executing:
    screen.fill((205, 144, 228))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            is_executing = False
            break

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                player_change_x = -0.1

            if e.key == pygame.K_RIGHT:
                player_change_x = 0.1

    player_x += player_change_x

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    enemy_x += enemy_change_x

    if enemy_x <= 0:
        enemy_x = 0
        enemy_change_x *= -1
        enemy_y += 20
    elif enemy_x >= 736:
        enemy_x = 736
        enemy_change_x *= -1
        enemy_y += 20

    update_enemy(enemy_x, enemy_y)

    update_player(player_x, player_y)
    pygame.display.update()

