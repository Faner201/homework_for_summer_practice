import re
import pygame as pg
from math import sin, cos, radians

class MultiplicationTable():
    def __init__(self) -> None:
        self.running = False
        self.size = 400
        self.step = 0
        self.speed = 0
        self.color = pg.Color(255, 0, 0)
        self.hue = 0.0
        self.clock = pg.time.Clock()
        self.points = [self.get_coord(i) for i in range(360)]
        self.screen = pg.display.set_mode((self.size, self.size))


    def launch(self) -> None:
        self.running = True
        pg.init()
        while self.running:
            self.input()
            self.update_screen()
            self.render()
        pg.quit()


    def input(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        self.speed = 0.001 if self.speed == 0 else 0


    def update_screen(self) -> None:
        self.step += self.speed * self.clock.tick(60)
        hsva = self.color.hsva
        self.color.hsva = ((self.step * 45) % 360, hsva[1], hsva[2], hsva[3])


    def get_coord(self, index: int) -> tuple[int, int]:
        half = self.size // 2
        return (int(cos(radians(index)) * half * 0.9) + half, int(sin(radians(index)) * half * 0.9) + half)

    
    def render(self) -> None:
        self.screen.fill("black")
        for i in range(360):
            start = self.get_coord(i)
            end = self.get_coord(i * self.step)
            pg.draw.line(self.screen, self.color, start, end)
        pg.display.flip()

    
def main():
    program = MultiplicationTable()
    program.launch()


main()

