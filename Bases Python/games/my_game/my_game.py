import pygame

screen = pygame.display.set_mode((800, 600))

is_executing = True

while is_executing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            is_executing = False
            break

