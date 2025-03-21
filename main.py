import pygame
import os
import random
from pygame.locals import *
from sys import exit


pygame.init()


WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meu game na linguagem Python")


fonte = pygame.font.SysFont("arial", 30, True, False)


menu_opcoes = ["Novo Jogo", "Carregar Jogo", "Configurações", "Sobre", "Sair"]
menu_index = 0


backgroundGame = pygame.transform.scale(pygame.image.load(os.path.join("Python-Game", "image", "Background", "city 1", "1.png")).convert_alpha(), (WIDTH, HEIGHT))
image_Person = pygame.transform.scale(pygame.image.load(os.path.join("Python-Game", "image", "Person", "Corvette", "Idle.png")).convert_alpha(), (70, 70))
image_Missil = pygame.transform.scale(pygame.image.load(os.path.join("Python-Game", "image", "Person", "Bomber", "Charge_1.png")).convert_alpha(), (20, 20))
image_Enemy = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Python-Game", "image", "Person", "Fighter", "Idle.png")).convert_alpha(), (70, 70)), -180)

def iniciar_jogo():
    global pontos
   
    pos_player_x, pos_player_y = 200, 300
    pos_enemy_x, pos_enemy_y = 1280, random.randint(50, 670)
    pos_x_missil, pos_y_missil, vel_x_missil = pos_player_x + 30, pos_player_y + 30, 0
    triggered = False
    cooldown_missil = 0 
    pontos = 3  
    rodando = True
    clock = pygame.time.Clock()

    while rodando:
        screen.blit(backgroundGame, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

       
        tecla = pygame.key.get_pressed()
        if tecla[K_UP] and pos_player_y > 1:
            pos_player_y -= 5
            if not triggered:
                pos_y_missil -= 5

        if tecla[K_DOWN] and pos_player_y < HEIGHT - 70:
            pos_player_y += 5
            if not triggered:
                pos_y_missil += 5

        
        if tecla[K_SPACE] and not triggered and cooldown_missil == 0:
            triggered = True
            vel_x_missil = 15
            cooldown_missil = 20 

        
        if cooldown_missil > 0:
            cooldown_missil -= 1

        
        pos_enemy_x -= 10
        if pos_enemy_x < -70:  
            pontos -= 1
            pos_enemy_x = 1280
            pos_enemy_y = random.randint(50, 670)

      
        if triggered:
            pos_x_missil += vel_x_missil
        else:
            pos_x_missil = pos_player_x + 30
            pos_y_missil = pos_player_y + 30

       
        if pos_x_missil > WIDTH:
            triggered = False
            cooldown_missil = 10  

       
        rect_missil = pygame.Rect(pos_x_missil, pos_y_missil, 20, 20)
        rect_enemy = pygame.Rect(pos_enemy_x, pos_enemy_y, 70, 70)
        rect_player = pygame.Rect(pos_player_x, pos_player_y, 70, 70)

        
        if rect_missil.colliderect(rect_enemy):
            pontos += 1 
            triggered = False  
            pos_x_missil = pos_player_x + 30
            pos_enemy_x = 1280 
            pos_enemy_y = random.randint(50, 670)

        
        if rect_enemy.colliderect(rect_player):
            pontos -= 1 
            pos_enemy_x = 1280  
            pos_enemy_y = random.randint(50, 670)

      
        if pontos <= 0:
            return  

       
        screen.blit(image_Enemy, (pos_enemy_x, pos_enemy_y))
        screen.blit(image_Missil, (pos_x_missil, pos_y_missil))
        screen.blit(image_Person, (pos_player_x, pos_player_y))

        
        score = fonte.render(f'Pontos: {pontos}', True, (255, 255, 255))
        screen.blit(score, (50, 50))

        pygame.display.update()
        clock.tick(60)


def desenhar_menu():
    screen.fill((0, 0, 0))
    for i, opcao in enumerate(menu_opcoes):
        cor = (255, 255, 255) if i == menu_index else (100, 100, 100)
        texto = fonte.render(opcao, True, cor)
        screen.blit(texto, (WIDTH//2 - 100, HEIGHT//2 + i * 40))
    pygame.display.update()


while True:
    menu_index = 0  

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    menu_index = (menu_index - 1) % len(menu_opcoes)
                if event.key == K_DOWN:
                    menu_index = (menu_index + 1) % len(menu_opcoes)
                if event.key == K_RETURN: 
                    if menu_opcoes[menu_index] == "Novo Jogo":
                        rodando = False  
                    elif menu_opcoes[menu_index] == "Sair":
                        pygame.quit()
                        exit()
        
        desenhar_menu()

   
    iniciar_jogo()
