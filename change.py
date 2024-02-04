from functions import load_image
import pygame


class Change:
    def __init__(self):
        self.image = load_image("change_circle.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image_rect = self.image.get_rect(topleft=(550, 510))
        font = pygame.font.Font(None, 30)
        self.background = [font.render("Схема", True, pygame.Color("#000000")),
                           font.render("Спутник", True, pygame.Color('#000000')),
                           font.render("Гибрид", True, pygame.Color('#000000'))]
        self.n = 0

    def count(self, pos):
        if self.image_rect.collidepoint(pos):
            self.n += 1
            if self.n == 3:
                self.n = 0
            return True
        return False

    def update(self, screen):
        screen.blit(self.background[self.n], (472, 515))
        screen.blit(self.image, (550, 510))
