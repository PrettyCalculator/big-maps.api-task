import pygame
import requests
import os


def get_image():
    map_file = 'map.png'
    resp = requests.get(api_server, map_params)
    with open('response.json', 'wb') as file:
        file.write(resp.content)
    with open(map_file, "wb") as file:
        file.write(resp.content)
    img = pygame.image.load(map_file)
    os.remove(map_file)
    return img


api_server = "http://static-maps.yandex.ru/1.x/?"
map_params = {
    'll': '56.049898,53.449593',
    'spn': '0.002,0.002',
    'l': 'map',
    'pt': '56.049898,53.449593,flag'
}

image = get_image()
