import pygame
import os

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x, y))

pygame.display.set_caption('Meu game na linguagem Python')

background_name = 'bamboo bridge.png'

image_path = os.path.join('Python-Game', 'image', 'Background', '1', background_name)

backgroundGame = pygame.image.load(image_path).convert_alpha()

backgroundGame = pygame.transform.scale(backgroundGame, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(backgroundGame, (0,0))

    rel_x = x % backgroundGame.get_rect().width
    screen.blit(backgroundGame, (rel_x - backgroundGame.get_rect().width,0))

    if rel_x < 1280:
        screen.blit(backgroundGame, (rel_x, 0 ))
    
    x -= 1
    pygame.display.update()

pygame.quit()
