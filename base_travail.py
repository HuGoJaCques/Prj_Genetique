import pygame
import sys
import random
from FoodItem import GreenPoint
from Microbes import Microbe

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)



# Taille de la fenêtre et des cellules
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 480
CELL_SIZE = 1 # Taille des cases en pixels

# Nombre de microbes
NUM_MICROBES = 50


# Taille de la carte
MAP_WIDTH = WINDOW_WIDTH // CELL_SIZE
MAP_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

def main():
    pygame.init()    
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Microbe Simulation")
    clock = pygame.time.Clock()

    green_points = {(x, y): True for x in range(0, WINDOW_WIDTH, 5) for y in range(0, WINDOW_HEIGHT, 5)}
    microbes = [Microbe(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for _ in range(NUM_MICROBES)]

    screen.fill(BLACK)  # Remplir l'écran avec la couleur noire       
    

    # Dessiner les points verts restants
    for green_point in green_points:
        if green_points[green_point]==True:
            GreenPoint(*green_point).draw(screen)
    pygame.display.flip()

    running = True
    while running:
        nb_green_points = 0
        nb_green_pointsdel = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)  # Remplir l'écran avec la couleur noire     
        
        # Dessiner les points verts restants
        for green_point in green_points:
            
            if green_points[green_point]==True:
                nb_green_points +=1
                GreenPoint(*green_point).draw(screen)
            else:
                nb_green_pointsdel += 1

        # Dessiner et déplacer les microbes
        for microbe in microbes:
            microbe.draw(screen)
            microbe.move()
            microbe.eat_green_point(green_points)        
        
        print(nb_green_pointsdel)
        print(nb_green_points)
        pygame.display.flip()
        clock.tick(600)        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
