import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Calculadora')

# Colores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Área de la pantalla de resultados
display_rect = pygame.Rect(0, 0, width, 150)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar la pantalla de resultados
    pygame.draw.rect(screen, GRAY, display_rect)

    pygame.display.flip()
