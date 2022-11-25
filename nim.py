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
ms = pg.transform.scale(ms, (60, 100))

allumettes = []
for i in range(12):
    position = (10 + i * 20, 10)
    rec = pg.Rect((i*10, 0, 10 + i * 20, 10))
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