import os
import pygame
import requests

scale = ["0.0003,0.0003", "0.0005,0.0005", "0.001,0.001", "0.002,0.002", "0.003,0.003", "0.006,0.006", "0.015,0.015",
         "0.03,0.03", "0.07,0.07", "0.1,0.1", "0.5,0.5", "0.8,0.8"]


def get_image():
    map_file = 'map.png'
    resp = requests.get(api_server, map_params)
    with open(map_file, "wb") as file:
        file.write(resp.content)
    img = pygame.image.load('map.png')
    os.remove('map.png')
    return img


def big_small(n):
    global image
    map_params['spn'] = scale[n]
    image = get_image()


map_params = {
    'll': '56.049898,53.449593',
    'spn': '0.002,0.002',
    'l': 'map'
}

api_server = "http://static-maps.yandex.ru/1.x/?"

pygame.init()
screen = pygame.display.set_mode((600, 450))
image = get_image()
running = True
num = 3
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_PAGEUP]:
            if num > 0:
                num -= 1
                big_small(num)
        if keys[pygame.K_PAGEDOWN]:
            if num < 11:
                num += 1
                big_small(num)
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
