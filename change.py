from functions import load_image
import pygame


class Change:
    def __init__(self):
        self.image = load_image("change_circle.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        font = pygame.font.Font(None, 30)
        self.background = [font.render("Схема", True, pygame.Color("#000000")),
                           font.render("Спутник", True, pygame.Color('#000000')),
                           font.render("Гибрид", True, pygame.Color('#000000'))]
        self.n = 0

    def count(self, pos):
        if 558 < pos[0] < 569 and 506 < pos[1] < 530:
            self.n += 1
            if self.n == 3:
                self.n = 0
            return True
        return False

    def update(self, screen):
        screen.blit(self.background[self.n], (470, 515))
        screen.blit(self.image, (550, 510))
