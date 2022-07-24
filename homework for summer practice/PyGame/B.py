from turtle import width
import pygame as pg

def main():
    screen_size = width, height = 400, 400

    pg.init()

    screen = pg.display.set_mode(screen_size)

    initial_rect = pg.Rect(0, 0, 0, 0)
    movement = True
    drawing = False
    layers = []

    while movement:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                drawing = True
                initial_rect.update(event.pos, (0,0))
            if event.type == pg.MOUSEMOTION:
                initial_rect.size = (event.pos[0] - initial_rect.left, event.pos[1] - initial_rect.top)
            if event.type == pg.MOUSEBUTTONUP:
                drawing = False
                layer = initial_rect.copy()
                layer.normalize()
                layers.append(layer)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z and pg.key.get_mods() & pg.KMOD_CTRL:
                    if len(layers) > 0:
                        layers.pop()
            if event.type == pg.QUIT:
                movement = False
        
        screen.fill("black")
        for layer in layers:
            pg.draw.rect(screen, "white", layer, 4)
        if drawing:
            layer = initial_rect.copy()
            layer.normalize()
            pg.draw.rect(screen, "white", layer, 4)
        pg.display.flip()

    pg.quit()


main()

