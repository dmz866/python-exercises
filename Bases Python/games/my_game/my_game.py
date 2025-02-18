import io
import math
import random

import pygame
from pygame import mixer

'''
Create .exe
pyinstaller --clean --onefile --windowed my_game.py

copy resources files to dist (mp3, images, etc)

'''

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Set title, icon, background
pygame.display.set_caption('Space Invaders')

icon = pygame.image.load('space-man.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('space.jpg')

#Set music
mixer.music.load('bg-music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play()

#Player
player_img = pygame.image.load('spaceship.png')
player_x = 368
player_y = 510
player_change_x = 0.3
player_change_y = 0

#Enemies
enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0 ,736)
enemy_y = 10
enemy_change_x = 0.1

#Bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 368
bullet_y = 500
bullet_change_y = 1
bullet_visible = False

# Player Points
points = 0
points_x = 10
points_y = 10

#Fonts
def font_to_bytes(ff):
    with open(ff, 'rb') as f:
        tf = f.read()

    return io.BytesIO(tf)

font_bytes = font_to_bytes('FreeSansBold.ttf')
font = pygame.font.Font(font_bytes, 32)

def show_points(x, y):
    text = font.render(f'Points: {points}', True, (255, 255, 255))
    screen.blit(text, (x, y))

def update_player(x, y):
    screen.blit(player_img, (x, y))

def shoot_bullet(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_img, (x + 16, y + 10))

def update_enemy(x, y):
    screen.blit(enemy_img, (x, y))

def check_collisions(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return distance < 27

def game_over():
    global is_executing
    is_executing = False
    text = font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(text, (368, 250))

is_executing = True

while is_executing:
    screen.fill((205, 144, 228))
    #screen.blit(bg, (0,0))
    show_points(points_x, points_y)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            is_executing = False
            break

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                player_change_x = -0.3

            if e.key == pygame.K_RIGHT:
                player_change_x = 0.3

            if e.key == pygame.K_SPACE and not bullet_visible:
                s = mixer.Sound('shoot.mp3')
                s.play()
                bullet_x = player_x
                shoot_bullet(bullet_x, bullet_y)

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

    if bullet_y <= 0:
        bullet_visible = False
        bullet_y = 500

    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_change_y

    if check_collisions(enemy_x, enemy_y, bullet_x, bullet_y):
        s = mixer.Sound('collision.mp3')
        s.play()
        bullet_visible = False
        bullet_y = 500
        points += 1
        enemy_x = random.randint(0, 736)
        enemy_y = 0

    if check_collisions(enemy_x, enemy_y, player_x, player_y):
        game_over()

    update_enemy(enemy_x, enemy_y)

    update_player(player_x, player_y)
    pygame.display.update()

