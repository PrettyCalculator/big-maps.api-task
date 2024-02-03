import os
import pygame
import requests
from search import Search

scale = ["0.0003,0.0003", "0.0005,0.0005", "0.001,0.001", "0.002,0.002", "0.003,0.003", "0.006,0.006", "0.015,0.015",
         "0.03,0.03", "0.07,0.07", "0.1,0.1", "0.5,0.5", "0.8,0.8"]


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


def big_small(n):
    global image
    map_params['spn'] = scale[n]
    image = get_image()


def move_up():
    global image
    long = map_params['ll'].split(',')[0]
    lat = float(map_params['ll'].split(',')[1]) + float(map_params['spn'].split(',')[1]) * 1.5
    if lat < 84:
        map_params['ll'] = ','.join([long, str(lat)])
        image = get_image()


def move_down():
    global image
    long = map_params['ll'].split(',')[0]
    lat = float(map_params['ll'].split(',')[1]) - float(map_params['spn'].split(',')[1]) * 1.5
    if lat > -84:
        map_params['ll'] = ','.join([long, str(lat)])
        image = get_image()


def move_left():
    global image
    lat = map_params['ll'].split(',')[1]
    long = float(map_params['ll'].split(',')[0]) - float(map_params['spn'].split(',')[1]) * 3
    if long > -179:
        map_params['ll'] = ','.join([str(long), lat])
        image = get_image()


def move_right():
    global image
    lat = map_params['ll'].split(',')[1]
    long = float(map_params['ll'].split(',')[0]) + float(map_params['spn'].split(',')[1]) * 3
    if long < 179:
        map_params['ll'] = ','.join([str(long), lat])
        image = get_image()


map_params = {
    'll': '56.049898,53.449593',
    'spn': '0.002,0.002',
    'l': 'map'
}
api_server = "http://static-maps.yandex.ru/1.x/?"
pygame.init()
screen = pygame.display.set_mode((600, 550))
image = get_image()
search = Search()
background_image = pygame.Surface((600, 100))
background_image.fill('#FFEFD5')
running = True
num = 3
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            search.get_input(event.pos)
        if keys[pygame.K_PAGEUP]:
            if num > 0:
                num -= 1
                big_small(num)
        if keys[pygame.K_PAGEDOWN]:
            if num < 11:
                num += 1
                big_small(num)
        if keys[pygame.K_UP]:
            move_up()
        if keys[pygame.K_DOWN]:
            move_down()
        if keys[pygame.K_LEFT]:
            move_left()
        if keys[pygame.K_RIGHT]:
            move_right()
    screen.blit(image, (0, 0))
    screen.blit(background_image, (0, 450))
    search.update(screen)
    pygame.display.flip()

pygame.quit()
