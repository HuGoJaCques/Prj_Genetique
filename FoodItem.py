import pygame
import random

GREEN = (0,255,0)
class GreenPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):      
        pygame.draw.circle(screen, GREEN, (self.x, self.y), 2)
  