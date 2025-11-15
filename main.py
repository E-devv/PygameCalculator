import pygame
import sys
from config import * # Importamos los nuevos colores y dimensiones
from logic import CalculatorLogic
from button import Button, lerp # Necesitamos lerp para el efecto del texto

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Calculadora Neon')

# Instancias
logic = CalculatorLogic()
# Usamos Arial Bold para asegurar que los símbolos se vean bien
display_font = pygame.font.SysFont("Arial", 65, bold=True)

# --- CONFIGURACIÓN DE BOTONES ---
buttons = []

# Layout de la calculadora
layout = [
    ['C', '<', '%', '÷'],
    ['7', '8', '9', 'x'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['00', '0', '.', '=']
]

# Cálculos de posición
margin = 15 
cols = 4
# Calculamos el ancho dinámicamente basado en el ancho de pantalla
btn_width = (SCREEN_WIDTH - (margin * (cols + 1))) // cols
btn_height = 80 # Altura fija para los botones
start_y = 180   # Dejamos espacio para la pantalla de resultados

for row_idx, row_values in enumerate(layout):
    for col_idx, text in enumerate(row_values):
        # Posición X e Y
        x = margin + (col_idx * (btn_width + margin))
        y = start_y + (row_idx * (btn_height + margin))
        
        # --- LÓGICA DE COLORES NEON ---
        if text == '=':
             # El igual: Magenta Neon (destacado)
            c_base, c_hover, c_active = BTN_COLOR_MISC, BTN_HOVER_MISC, BTN_ACTIVE_MISC
        elif text in ['C', '<', '%']:
             # Funciones especiales: Magenta Neon
            c_base, c_hover, c_active = BTN_COLOR_MISC, BTN_HOVER_MISC, BTN_ACTIVE_MISC
        elif text in ['÷', 'x', '-', '+']:
             # Operadores: Cian Neon
             c_base, c_hover, c_active = BTN_COLOR_OP, BTN_HOVER_OP, BTN_ACTIVE_OP
        else:
            # Números: Morado Neon
            c_base, c_hover, c_active = BTN_COLOR_NUM, BTN_HOVER_NUM, BTN_ACTIVE_NUM

        # Crear el botón
        btn = Button(screen, text, (x, y), (btn_width, btn_height), c_base, c_hover, c_active)
        buttons.append(btn)

# --- VARIABLES DE ANIMACIÓN TEXTO ---
clock = pygame.time.Clock()
text_scale = 1.0
last_text = "0"

# --- BUCLE PRINCIPAL ---
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 1. Obtener texto actual y manejar animación "Pop"
    current_text = logic.get_display_text()
    
    if current_text != last_text:
        text_scale = 1.4 # Zoom al cambiar el texto
        last_text = current_text
    
    # Volver suavemente a escala 1.0
    text_scale = lerp(text_scale, 1.0, 0.2)

    # 2. Dibujar Fondo
    screen.fill(BG_COLOR)

    # 3. Actualizar y Dibujar Botones
    for btn in buttons:
        if btn.process_input(events): # Si fue presionado
            logic.press_key(btn.text)
        btn.update() # Animar color y tamaño
        btn.draw()

    # 4. Dibujar Pantalla de Resultados (Estilo Monitor)
    display_rect = pygame.Rect(15, 20, SCREEN_WIDTH-30, 140)
    # Fondo del display un poco más claro que el fondo general
    pygame.draw.rect(screen, (20, 15, 30), display_rect, border_radius=20)
    # Borde fino del display
    pygame.draw.rect(screen, (50, 40, 60), display_rect, width=2, border_radius=20)
    
    # Renderizar texto del resultado
    base_surf = display_font.render(current_text, True, RESULT_COLOR)
    
    # Aplicar el efecto de escala (Pop)
    new_w = int(base_surf.get_width() * text_scale)
    new_h = int(base_surf.get_height() * text_scale)
    
    # Evitar crash si el ancho es 0 (aunque es raro)
    if new_w > 0 and new_h > 0:
        scaled_surf = pygame.transform.smoothscale(base_surf, (new_w, new_h))
    else:
        scaled_surf = base_surf
    
    # Alinear a la derecha verticalmente centrado
    text_rect = scaled_surf.get_rect(midright=(display_rect.right - 20, display_rect.centery))
    screen.blit(scaled_surf, text_rect)

    pygame.display.flip()
    clock.tick(60)