import os
import sys

import pygame
import requests



def get_image():
    map_file = 'map.png'
    resp = requests.get(api_server, map_params)
    with open(map_file, "wb") as file:
        file.write(resp.content)
    img = pygame.image.load('map.png')
    os.remove('map.png')
    return img


def move_up():
    print('да')
    long = map_params['ll'].split()[0]
    lat = str(float(map_params['ll'].split(',')[1]) + float(map_params['spn'].split(',')[1]))
    map_params['ll'] = ','.join([long, lat])


def big(n):
    map_request = "http://static-maps.yandex.ru/1.x/?ll=56.049898%2C53.449593&spn=" + f"{n}" + "," + f"{n}" + "&l=map"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    print(n)
    if n > 0:
        return n
    return 0

def small(n):
    map_request = "http://static-maps.yandex.ru/1.x/?ll=56.049898%2C53.449593&spn=" + f"{n}" + "," + f"{n}" + "&l=map"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    print(n)
    if n > 0:
        return n
    return 0

map_params = {
    'll': '56.049898,53.449593',
    'spn': '0.001,0.002',
    'l': 'map'
}

api_server = "http://static-maps.yandex.ru/1.x/?"

pygame.init()
screen = pygame.display.set_mode((600, 450))
image = get_image()
screen.blit(image, (0, 0))
pygame.display.flip()
running = True
a = 0.002
while running:
    num = 0.001
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_PAGEUP]:
            num = a - 0.001
            a = big(num)
            image = get_image()
        if keys[pygame.K_PAGEDOWN]:
            print(21)
            num = a + 0.01
            a = big(num)
            image = get_image()
    screen.blit(image, (0, 0))

pygame.quit()
