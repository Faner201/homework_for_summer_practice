import pygame as pg
from random import random

class HalfDuper():
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((400,400))
        self.running = False
        self.field_size = 10
        self.field = []
        self.font: pg.font.Font


    def create_field(self) -> None:
        for y in range(self.field_size):
            self.field.append([])
            for x in range(self.field_size):
                value = "*" if random() > 0.9 else "_"
                self.field[y].append(value)


    def show_field(self) -> None:
        for y in range(self.field_size):
            for x in range(self.field_size):
                rect = pg.Rect(40 * x, 40 * y, 40, 40)
                if self.field[y][x] == "*":
                    pg.draw.rect(self.screen, "red", rect)
                pg.draw.rect(self.screen, "white", rect, 2)
        pg.display.flip()


    def start(self) -> None:
        self.running = True
        pg.init()
        pg.font.init()
        self.font = pg.font.Font(None, 28)
        self.create_field()
        self.show_field()


    def input(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.setting_cell_value(event.pos)


    def get_number(self, x, y) -> int:
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= y + i < self.field_size and 0 <= x + j < self.field_size:
                    if self.field[y + i][x + j] == '*':
                        count += 1
        return count

    
    def setting_cell_value(self, pos) -> None:
        x, y = pos[0] // 40, pos[1] // 40
        if self.field[y][x] != "_":
            return
        number = self.get_number(x, y)
        self.field[y][x] = str(number)
        text = self.font.render(str(number), False, "white")
        self.screen.blit(text, (x * 40 + 15, y * 40 + 15))
        pg.display.flip()


    def quit(self) -> None:
        self.running = True
        pg.init()


    def launch(self) -> None:
        self.start()
        while self.running:
            self.input()
        self.quit()


def main():
    programm = HalfDuper()
    programm.launch()


main()