import pygame
import random

# Taille de la fenêtre et des cellules
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 480
CELL_SIZE = 1 # Taille des cases en pixels

#color
BLUE = (0, 0,255)
BLACK = (0, 0, 0)

class Microbe:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), 5)

    def move(self):
        self.x += random.randint(-5, 5)
        self.y += random.randint(-5, 5)
        self.x = max(0, min(self.x, WINDOW_WIDTH))
        self.y = max(0, min(self.y, WINDOW_HEIGHT))

    def eat_green_point(self, green_points):
        for green_point in green_points:
            if (self.x, self.y) == green_point:
                green_points[green_point] = False
            
            
