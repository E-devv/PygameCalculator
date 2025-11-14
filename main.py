import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Calculadora')

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
