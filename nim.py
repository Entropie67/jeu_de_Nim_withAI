import pygame as pg

pg.init()


(L, H) = (900, 600)
COULEUR_FOND = (0, 255, 255)


screen = pg.display.set_mode((L, H))
pg.display.set_caption('Jeu de Nim (AI)')
screen.fill(COULEUR_FOND)


# load matchstick (ms)
ms = pg.image.load('ms.png').convert_alpha()
ms = pg.transform.scale(ms, (50, 100))
for i in range (12):
    screen.blit(ms, (10 + i * 20, 10))
pos = ms.get_rect()
print(pos)


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    pg.display.update()
    pg.display.flip()