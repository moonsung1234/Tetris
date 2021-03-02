
from objects import Objects
import pygame as pg
import numpy as np
import random
import sys

class Tetris :
    def __init__(self, size) :
        self.SIZE = size
        self.FPS = 10
        self.BC = (255, 255, 255)
        self.CHUNK = (int(self.SIZE[0] / 10), int(self.SIZE[1] / 30))

        # will be more
        self.SHAPE1_INT, self.SHAPE1_COLOR = 1, (255, 0, 0)
        self.SHAPE2_INT, self.SHAPE2_COLOR = 2, (0, 255, 0)

        self.SHAPE1 = [
            [self.SHAPE1_INT for _ in range(4)],
            [0, 0, 0, 0]
        ]
        self.SHAPE2 = [
            [self.SHAPE2_INT],
            [self.SHAPE2_INT],
            [self.SHAPE2_INT],
            [self.SHAPE2_INT],
            [0]
        ]

        self.pg = pg
        self.map = [
            [0 for _ in range(int(self.SIZE[0] / self.CHUNK[0]))] for _ in range(int(self.SIZE[1] / self.CHUNK[1]))
        ]
        self.objects = []


    def __drawBlock(self, x, y, w, h, color) :
        self.pg.draw.rect(
            self.screen,
            color,
            (x, y, w, h)
        )

    def __drawMap(self) :
        for j, line in enumerate(self.map) :
            for i, block in enumerate(line) :
                if block == self.SHAPE1_INT :
                    self.__drawBlock(i * self.CHUNK[0], j * self.CHUNK[1], self.CHUNK[0], self.CHUNK[1], self.SHAPE1_COLOR)

                elif block == self.SHAPE2_INT :
                    self.__drawBlock(i * self.CHUNK[0], j * self.CHUNK[1], self.CHUNK[0], self.CHUNK[1], self.SHAPE2_COLOR)

    def __checkFullLine(self) :
        for j, line in enumerate(self.map) :
            for i, block in enumerate(line) :
                if block == 0 :
                    break

                elif i == len(line) - 1 :
                    del self.map[j]
                    self.map.insert(0, [0 for _ in range(len(line))])

        return True

    def show(self) :
        self.pg.init()
        self.pg.display.set_caption("Tetris!")
        self.screen = self.pg.display.set_mode(self.SIZE)
        self.clock = self.pg.time.Clock()

        # pre work
        self.screen.fill(self.BC)

        # set objects
        random_state = random.randint(0, 1)

        self.objects.append(
            Objects(
                self.pg, 
                self.screen, 
                self.map, 
                self.SHAPE1 if random_state == 0 else self.SHAPE2 , 
                self.SHAPE1_INT if random_state == 0 else self.SHAPE2_INT ,
                self.SHAPE1_COLOR if random_state == 0 else self.SHAPE2_COLOR ,
                self.CHUNK
            )
        )

        while True :
            self.screen.fill(self.BC)
            
            for event in self.pg.event.get() :
                if event.type == self.pg.QUIT :
                    sys.exit(0)

                elif event.type == self.pg.KEYUP :
                    if event.key == self.pg.K_LEFT :
                        self.objects[-1].moveX(-1)

                    elif event.key == self.pg.K_RIGHT :
                        self.objects[-1].moveX(1)

            # someting will be in here
            self.__drawMap()
            
            if not self.objects[-1].draw() and self.__checkFullLine() :
                break

            self.pg.display.flip()
            self.clock.tick(self.FPS)

        self.show()

tetris = Tetris(
    (200, 600)
)
tetris.show()
        