import pygame as pg

pg.init()

AI = []

(L, H) = (900, 600)
COULEUR_FOND = (0, 255, 255)


screen = pg.display.set_mode((L, H))
pg.display.set_caption('Jeu de Nim (AI)')
screen.fill(COULEUR_FOND)


# load matchstick (ms)
ms = pg.image.load('ms.png').convert_alpha()
l = 60
h = 100
ms = pg.transform.scale(ms, (l, h))

allumettes = []
for i in range(12):
    rec = pg.Rect((10 + i*l, 0, l, h))
    screen.blit(ms, rec)
    allumettes.append(rec)

print(allumettes)
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    pg.display.update()
    pg.display.flip()