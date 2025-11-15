import pygame

def lerp(start, end, amount):
    return start + (end - start) * amount

def lerp_color(c1, c2, amount):
    return [int(start + (end - start) * amount) for start, end in zip(c1, c2)]

class Button:
    def __init__(self, surface, text, pos, size, color_base, color_hover, color_active):
        self.surface = surface
        self.text = text
        self.original_rect = pygame.Rect(pos, size) # Guardamos el tamaño original
        self.rect = self.original_rect.copy()       # Este es el que dibujaremos
        
        # Colores
        self.color_base = color_base
        self.color_hover = color_hover
        self.color_active = color_active
        self.current_color = list(color_base)
        self.target_color = color_base

        # Animación de Escala (Tamaño)
        self.scale = 1.0
        self.target_scale = 1.0
        
        self.is_pressed = False
        self.font = pygame.font.SysFont("Arial", 30, bold=True) # Fuente más segura

    def process_input(self, events):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.original_rect.collidepoint(mouse_pos)
        
        action = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if is_hovered:
                    self.is_pressed = True
                    self.target_scale = 0.90 # Se encoge al 90%
                    action = True
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.is_pressed = False
                self.target_scale = 1.0 # Vuelve a tamaño normal

        # Lógica de hover (si no está presionado)
        if not self.is_pressed:
            if is_hovered:
                self.target_color = self.color_hover
                self.target_scale = 1.05 # Crece un poquito (5%) al pasar el mouse
            else:
                self.target_color = self.color_base
                self.target_scale = 1.0
        else:
            self.target_color = self.color_active

        return action

    def update(self):
        # Animar color
        self.current_color = lerp_color(self.current_color, self.target_color, 0.2)
        
        # Animar escala (Efecto elástico)
        self.scale = lerp(self.scale, self.target_scale, 0.3)

    def draw(self):
        # Calcular el nuevo rectángulo basado en la escala
        w = int(self.original_rect.width * self.scale)
        h = int(self.original_rect.height * self.scale)
        
        anim_rect = pygame.Rect(0, 0, w, h)
        anim_rect.center = self.original_rect.center

        # 1. Relleno del botón (El color base oscuro)
        # Si está presionado, usamos el color brillante para rellenar (efecto flash)
        fill_color = self.color_active if self.is_pressed else self.current_color
        pygame.draw.rect(self.surface, fill_color, anim_rect, border_radius=15)
        
        # 2. EL EFECTO NEON: El borde siempre es del color "Active" (el brillante)
        # Esto hace que parezca que tiene un tubo de luz alrededor
        glow_color = self.color_active 
        pygame.draw.rect(self.surface, glow_color, anim_rect, width=3, border_radius=15)

        # Texto
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=anim_rect.center)
        self.surface.blit(text_surf, text_rect)