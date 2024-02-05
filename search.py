from functions import load_image
import pygame
import requests
import string
import settings as s


class Search:
    default_image = load_image('unhovered_string.png', -1)
    hovered_image = load_image('hovered_string.png', -1)
    acceptable_values = string.ascii_letters + 'йцукенгшщзхъфывапролджэячсмитьбю.,- ()1234567890)(*?:%;№"!'

    def __init__(self):
        self.available = False

        self.text = ''
        self.display_text = ''
        self.font = pygame.font.SysFont('Times New Roman', 25)
        self.text_image = self.font.render(self.display_text, True, 'black')
        self.text_image_pos = 10, 463

        self.address_font = pygame.font.SysFont('Times New Roman', 16)
        self.full_address = 'Адрес: '
        self.full_address_image = self.address_font.render(self.full_address, True, 'black')
        self.full_address_image_pos = 5, 540

        self.full_address1 = ''
        self.full_address_image1 = self.address_font.render(self.full_address1, True, 'black')
        self.full_address_image_pos1 = 5, 560

        self.image_pos = 0, 450
        self.image = Search.default_image
        self.image_rect = self.image.get_rect(topleft=self.image_pos)

        self.find_image_pos = 557, 468
        self.find_image = load_image('search_button.png')
        self.find_image_rect = self.find_image.get_rect(topleft=self.find_image_pos)

        self.res = load_image("delete.png")
        self.res = pygame.transform.scale(self.res, (30, 30))
        self.res_rect = self.res.get_rect(topleft=(5, 510))
        self.text1 = self.font.render("Сброс", True, pygame.Color("#000000"))

        self.on = load_image("turn_on.png")
        self.on = pygame.transform.scale(self.on, (30, 30))
        self.on_rect = self.on.get_rect(topleft=(280, 510))

        self.off = load_image("turn_off.png")
        self.off = pygame.transform.scale(self.off, (30, 30))
        self.off_rect = self.off.get_rect(topleft=(280, 510))

        self.text_turn = self.font.render("Почта", True, pygame.Color("#000000"))

        self.turn = False

        self.geocoder_params = {
            'apikey': "40d1649f-0493-4b70-98ba-98533de7710b",
            'geocode': '',
            'lang': 'ru_RU',
            'format': 'json'
        }
        self.server = "http://geocode-maps.yandex.ru/1.x/?"

    def update(self, screen):
        screen.blit(self.image, self.image_pos)
        screen.blit(self.find_image, self.find_image_pos)
        screen.blit(self.text_image, self.text_image_pos)
        screen.blit(self.full_address_image, self.full_address_image_pos)
        screen.blit(self.full_address_image1, self.full_address_image_pos1)
        screen.blit(self.text1, (40, 510))
        screen.blit(self.text_turn, (210, 510))
        screen.blit(self.res, (5, 510))
        if self.turn:
            screen.blit(self.on, (285, 510))
        if not self.turn:
            screen.blit(self.off, (285, 510))

    def click(self, pos):
        if self.res_rect.collidepoint(pos):
            s.map_params['pt'] = ""
            self.get_address_image('')
            s.image = s.get_image()

    def address(self, pos):
        if self.on_rect.collidepoint(pos) or self.off_rect.collidepoint(pos):
            if self.turn:
                self.turn = False
                self.find()
            else:
                self.turn = True
                self.find()

    def change_available(self):
        self.available = not self.available
        if self.available:
            self.image = Search.hovered_image
        else:
            self.image = Search.default_image

    def get_input(self, pos):
        if self.find_image_rect.collidepoint(pos):
            self.find()
        elif self.image_rect.collidepoint(pos):
            self.change_available()
        elif self.available:
            self.change_available()

    def find(self):
        if self.text:
            try:
                self.geocoder_params['geocode'] = self.text
                resp = requests.get(self.server, self.geocoder_params)
                coords = ','.join(
                    resp.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"][
                        "pos"].split())
                if not self.turn:
                    self.get_address_image(
                        resp.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
                            "metaDataProperty"][
                            "GeocoderMetaData"]["Address"]["formatted"])
                if self.turn:
                    self.get_address_image(
                        resp.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
                            "metaDataProperty"][
                            "GeocoderMetaData"]["Address"]["formatted"],
                        resp.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
                            "metaDataProperty"][
                            "GeocoderMetaData"]["Address"]["postal_code"])
                s.map_params['ll'] = coords
                s.map_params['pt'] = coords + ',flag'
                s.image = s.get_image()
            except Exception:
                print('ошибка')

    def text_processing(self, event):
        if event.key == pygame.K_BACKSPACE:
            print('удаляем')
            self.delete_char()
        elif event.key == pygame.K_RETURN:
            print('ищем')
            self.find()
        elif event.unicode.lower() in Search.acceptable_values:
            self.text += event.unicode
            self.display_text += event.unicode
            if len(self.display_text) >= 40:
                self.display_text = self.display_text[-40:]
            self.text_image = self.font.render(self.display_text, True, 'black')

    def delete_char(self):
        if self.text:
            self.text = self.text[:-1]
            self.display_text = self.display_text[:-1]
            self.text_image = self.font.render(self.display_text, True, 'black')

    def get_address_image(self, text, post=""):
        self.full_address = f'Адрес: {text}'
        self.full_address1 = f'{post}'
        self.full_address_image = self.address_font.render(self.full_address, True, 'black')
        self.full_address_image1 = self.address_font.render(self.full_address1, True, 'black')
