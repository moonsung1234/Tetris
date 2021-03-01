
from objects import Objects
import pygame as pg
import numpy as np
import random
import sys

class Tetris :
    def __init__(self, size) :
        self.SIZE = size
        self.FPS = 30
        self.BC = (255, 255, 255)
        self.CHUNK = (int(self.SIZE[0] / 20), int(self.SIZE[1] / 20))

        self.SHAPE1 = (
            (0, 0, 0, 0),
            (1, 1, 1, 1),
            (0, 0, 0, 0)
        )

        self.pg = pg
        self.objects = []

    def __initShape(self, shape) :
        _object = Objects(self.pg, self.screen, shape, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), self.CHUNK)

        return _object

    def __drawShape(self, _object) :
        is_move = _object.checkCrash()
        _object.draw()

        return is_move

    def show(self) :
        self.pg.init()
        self.pg.display.set_caption("Tetris!")
        self.screen = self.pg.display.set_mode(self.SIZE)
        self.clock = self.pg.time.Clock()

        # set objects
        self.objects.append(self.__initShape(self.SHAPE1))
        index_now = len(self.objects) - 1

        while True :
            self.screen.fill(self.BC)
            
            for event in self.pg.event.get() :
                if event.type == self.pg.QUIT :
                    sys.exit(0)

                elif event.type == self.pg.KEYUP :
                    if event.key == self.pg.K_RIGHT :
                        self.objects[index_now].moveSide(self.CHUNK[0])

                    elif event.key == self.pg.K_LEFT :
                        self.objects[index_now].moveSide(-self.CHUNK[0])

            # someting will be in here
            for i in range(index_now) :
               self.__drawShape(self.objects[i]) 

            if self.__drawShape(self.objects[index_now]) :
                break

            self.pg.display.flip()
            self.clock.tick(self.FPS)

        self.show()

tetris = Tetris(
    (400, 400)
)
tetris.show()
        