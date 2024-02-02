import os
import sys

import pygame
import requests

map_request = "http://static-maps.yandex.ru/1.x/?ll=56.049898%2C53.449593&spn=0.001," f"{0.002}" + "&l=map"
response = requests.get(map_request)
num = 0
n = 0.002


def functions(n):
    if n > num:
        n += 0.001
        print(n)
    else:
        n -= 0.001
    print(n)
    map_request = "http://static-maps.yandex.ru/1.x/?ll=56.049898%2C53.449593& +spn=0.001," + f"{n}" + "&l=map"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_PAGEUP]:
            functions(1)

pygame.quit()
os.remove(map_file)
