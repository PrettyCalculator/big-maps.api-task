import pygame
from search import Search
import settings as s
from change import Change

scale = ["0.0003,0.0003", "0.0005,0.0005", "0.001,0.001", "0.002,0.002", "0.003,0.003", "0.006,0.006", "0.015,0.015",
         "0.03,0.03", "0.07,0.07", "0.1,0.1", "0.5,0.5", "0.8,0.8"]
background = ["map", "sat", "sat,skl"]


def big_small(n):
    s.map_params['spn'] = scale[n]
    s.image = s.get_image()


def move_up():
    map_params = s.map_params
    long = map_params['ll'].split(',')[0]
    lat = float(map_params['ll'].split(',')[1]) + float(map_params['spn'].split(',')[1]) * 1.5
    if lat < 84:
        map_params['ll'] = ','.join([long, str(lat)])
        s.image = s.get_image()


def move_down():
    map_params = s.map_params
    long = map_params['ll'].split(',')[0]
    lat = float(map_params['ll'].split(',')[1]) - float(map_params['spn'].split(',')[1]) * 1.5
    if lat > -84:
        map_params['ll'] = ','.join([long, str(lat)])
        s.image = s.get_image()


def move_left():
    map_params = s.map_params
    lat = map_params['ll'].split(',')[1]
    long = float(map_params['ll'].split(',')[0]) - float(map_params['spn'].split(',')[1]) * 3
    if long > -179:
        map_params['ll'] = ','.join([str(long), lat])
        s.image = s.get_image()


def move_right():
    map_params = s.map_params
    lat = map_params['ll'].split(',')[1]
    long = float(map_params['ll'].split(',')[0]) + float(map_params['spn'].split(',')[1]) * 3
    if long < 179:
        map_params['ll'] = ','.join([str(long), lat])
        s.image = s.get_image()


pygame.init()
screen = pygame.display.set_mode((600, 550))
background_image = pygame.Surface((600, 150))
background_image.fill('#FFEFD5')
running = True
num = 3
n1 = 0
search = Search()
change = Change()
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            search.get_input(event.pos)
        if event.type == pygame.KEYDOWN and search.available:
            search.text_processing(event)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            w = change.count(event.pos)
            w1 = search.click(event.pos)
            w2 = search.address(event.pos)

    screen.blit(s.image, (0, 0))
    screen.blit(background_image, (0, 450))
    search.update(screen)
    change.update(screen)
    pygame.display.flip()

pygame.quit()
