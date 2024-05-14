import pygame
import math
import random

class BOLA:
    def __init__(self, x, y, diry = 1, dirx = 1, ang = 45, radio = 10, vel = 13): #diry = 1, dirx = 1
        self.golpe_pala = pygame.mixer.Sound("ping_pong_ball.wav")
        self.x = x
        self.y = y
        self.radio = radio
        self.vel = vel * 0.02
        self.diry = diry
        self.dirx = dirx
        self.angulo = ang
    
    def update(self, has_perdut, p_left, p_right, left_points, right_points):
        if self.x <= p_left.posicion_x + 5 + self.radio and self.x >= p_left.posicion_x and p_left.posicion_y <= self.y <= p_left.posicion_y + 100: #and p_left.posicion_x > self.x:
            #self.diry *= -1
            #self.dirx *= -1
            self.change_angle_pala()
            pygame.mixer.Sound.play(self.golpe_pala, 1, 1)
      
        elif self.x >= p_right.posicion_x - 5 - self.radio and self.x <= p_right.posicion_x and p_right.posicion_y <= self.y <= p_right.posicion_y + 100: #and p_right.posicion_x < self.x:
            #self.diry *= -1
            #self.dirx *= -1
            self.change_angle_pala()
            pygame.mixer.Sound.play(self.golpe_pala,  1, 1)
        
        
        elif self.y <= 25+self.radio:
            #self.diry *= -1
            self.change_angle_pared()
            #print("Choque techo")
            
        elif self.y >= 575-self.radio:
            #self.diry *= -1
            self.change_angle_pared()
            #print("Choque suelo")
            
        if self.x < p_left.posicion_x - 50:
            p_right.puntos += 1
            right_points += 1
            return [True, left_points, right_points]
        
        if self.x > p_right.posicion_x + 50:
            p_left.puntos += 1
            left_points += 1
            return [True, left_points, right_points]
            
        self.x += self.vel * math.cos(math.radians(self.angulo))# * self.dirx
        self.y += self.vel * math.sin(math.radians(self.angulo))# * self.diry
        return[has_perdut, left_points, right_points]
    
    
    def change_angle_pared(self):
        self.angulo = (180 - 2*self.angulo)/2 + 90
        if self.angulo >= 180:
            self.angulo = self.angulo - 180
        elif self.angulo <= 180: 
            self.angulo = self.angulo + 180
    
    
    def change_angle_pala(self):
        self.angulo = (180 - 2*self.angulo)/2 - 90
        if self.angulo >= 180:
            self.angulo = self.angulo - 180
        elif self.angulo <= 180: 
            self.angulo = self.angulo + 180

