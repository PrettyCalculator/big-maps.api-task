from functions import load_image


class Search:
    default_image = load_image('unhovered_string.png', -1)
    hovered_image = load_image('hovered_string.png', -1)

    def __init__(self):
        self.text = ''
        self.available = False
        self.image = Search.default_image
        self.image_rect = self.image.get_rect()
        self.find_image = load_image('search_button.png')
        self.find_image_rect = self.find_image.get_rect()
        print(self.image.get_rect())

    def update(self, screen):
        screen.blit(self.image, (0, 450))
        screen.blit(self.find_image, (557, 468))

    def get_input(self, pos):
        print(pos)
        if self.image_rect.collidepoint(pos):
            print('da')
            self.image = Search.hovered_image
