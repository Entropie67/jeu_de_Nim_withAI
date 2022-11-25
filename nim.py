import pygame as pg

pg.init()

(L, H) = (600, 300)

screen = pg.display.set_mode((L, H))
pg.display.set_caption('Jeu de Nim (AI)')
pg.display.update()

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False