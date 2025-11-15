import pygame

class Button:
    def __init__(self, surface, text, pos, size, color_base, color_hover):
        self.surface = surface
        self.text = text
        self.pos = pos
        self.size = size
        self.color_base = color_base
        self.color_hover = color_hover
        self.rect = pygame.Rect(self.pos, self.size)
        self.font = pygame.font.Font(None, 36)
        self.hovered = False

    def draw(self):
        color = self.color_hover if self.hovered else self.color_base
        pygame.draw.rect(self.surface, color, self.rect)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.surface.blit(text_surf, text_rect)

    def is_over(self, pos_mouse):
        self.hovered = self.rect.collidepoint(pos_mouse)
        return self.hovered
