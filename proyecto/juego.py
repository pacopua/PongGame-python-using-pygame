import pygame
import pygame.freetype

from personaje import Personaje as p
import random

from bola import BOLA as b

pygame.init()

#console
font = pygame.font.Font('PressStart2P-Regular.ttf', 24)
text = font.render('3 - 3', True, (255, 255, 255))

print(text)

amplada_finestra = 800
altura_finestra = 600
screen = pygame.display.set_mode([amplada_finestra, altura_finestra])
pygame.display.set_caption("PONG")

left_points = 0
right_points = 0

has_perdut = False

while left_points < 3 and right_points < 3:
    ran_list = [random.uniform(-80,-30), random.uniform(30, 80), random.uniform(-170,-120), random.uniform(120, 170)]
    pelota = b(random.uniform(350, 450), random.uniform(250, 350), random.choice([1, -1]), random.choice([1, -1]), random.choice(ran_list), radio = 10, vel = 15)#random.choice([1, -1]), random.choice([1, -1])
    #print("pos_pilota(x, y): " + str(pelota.x) + " " + str(pelota.y))
    p_left = p(250, 50)
    p_right = p(250, 750)
    
    while not has_perdut:
        text = font.render(str(left_points) + ' - ' + str(right_points), True, (255, 255, 255))
        
        screen.fill((0, 0, 0))
        screen.blit(text, (350, 35))
        pygame.draw.line(screen, (255, 255, 255), (0, 25), (800, 25))
        pygame.draw.line(screen, (255, 255, 255), (0, 575), (800, 575))
        
        pygame.draw.rect(screen, (255, 255, 255), (p_left.posicion_x, p_left.posicion_y, 10, 100))
        pygame.draw.rect(screen, (255, 255, 255), (p_right.posicion_x, p_right.posicion_y, 10, 100))
        
        pygame.draw.circle(screen, (255, 255, 255), (pelota.x, pelota.y), pelota.radio)
        
        for event in pygame.event.get():
            
            #if event.type == pygame.KEYDOWN:
                #print(pygame.key.name(event.key))
            if event.type == pygame.QUIT:
                has_perdut = True
                right_points = 999
                left_points = 999
            
                
        tecla = pygame.key.get_pressed()
        
        p_right.posicion_y += (- tecla[pygame.K_UP] + tecla[pygame.K_DOWN]) * 0.35
        p_left.posicion_y += (- tecla[pygame.K_w] + tecla[pygame.K_s]) * 0.35
        
        pygame.display.flip()
        
        p_left.update()
        p_right.update()
        has_perdut, left_points, right_points = pelota.update(has_perdut, p_left, p_right, left_points, right_points)
        
    pygame.time.wait(150)
    has_perdut = False