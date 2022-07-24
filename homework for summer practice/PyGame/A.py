import pygame as pg

def main():
    print("Пожалуйста введите размер окна и количество клеток:")
    screen_size, number_cells = map(int, input().split())
    size = screen_size / number_cells

    pg.init()
    screen = pg.display.set_mode((screen_size, screen_size))

    for y in range(number_cells):
        for x in range(number_cells):
            color = "black" if (x + y) % 2 == 0 else "white"
            pg.draw.rect(screen, color, (size * x, size * y, size, size))

    pg.display.flip()

    while pg.event.wait().type != pg.QUIT:
        pass

    pg.quit()


main()

