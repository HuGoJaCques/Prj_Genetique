import pygame
import sys
import random
from FoodItem import GreenPoint
from Microbes import Microbe

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Taille de la fenêtre et des cellules
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 480
CELL_SIZE = 1 # Taille des cases en pixels
nbr_food_per_tick = 100


# Nombre de microbes
NUM_MICROBES = 50


def main():
    pygame.init()    
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Microbe Simulation")
    clock = pygame.time.Clock()
    list_of_lists=[[0 for i in range(WINDOW_WIDTH)] for j in range(WINDOW_HEIGHT)]
    microbes = [Microbe(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for _ in range(NUM_MICROBES)]

    screen.fill(BLACK)  # Remplir l'écran avec la couleur noire       
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)  # Remplir l'écran avec la couleur noire     
        
        # Dessiner les points verts restants
        for i in range(nbr_food_per_tick):
            x = random.randint(0,WINDOW_WIDTH-1)
            y = random.randint(0,WINDOW_HEIGHT-1)
            max = 100
            counter = 0
            while list_of_lists[y][x] == 1 and counter < max:
                counter += 1
                x = random.randint(0,WINDOW_WIDTH-1)
                y = random.randint(0,WINDOW_HEIGHT-1)
            list_of_lists[y][x] = 1

        # dessiner la nouriture
        for x in range(WINDOW_WIDTH):
            for y in range(WINDOW_HEIGHT):
                if list_of_lists[y][x]>0:
                    pygame.draw.circle(screen, GREEN, (x,y), 2)
                #if list_of_lists[y][x]<0:
                #    pygame.draw.circle(screen, RED, (x,y), 2)              

        # Dessiner et déplacer les microbes
        microbes = [element for element in microbes if not element.isdead() ]

        for microbe in microbes:
            microbe.move()
            microbe.eat_green_point(list_of_lists)
            microbe.draw(screen)
                   
        
        pygame.display.flip()
        clock.tick(600)        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
