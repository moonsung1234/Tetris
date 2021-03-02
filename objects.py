
import numpy as np
import time

class Objects :
    def __init__(self, pg, screen, _map, shape, shape_int, shape_color, chunk) :
        self.SHAPE = np.array(shape)
        self.SHAPE_INT = shape_int
        self.SHAPE_COLOR = shape_color
        self.CHUNK = chunk
        self.IS_MOVE = True

        self.x = 0
        self.y = 0
        self.pg = pg
        self.screen = screen
        self.map = _map

    def __init(self) :
        for j, line in enumerate(self.SHAPE) :
            for i, block in enumerate(line) :
                if self.y + j <= len(self.map) - 1 : 
                    self.map[self.y + j][self.x + i] = 0

    def __draw(self) :
        for j, line in enumerate(self.SHAPE) :
            for i, block in enumerate(line) :
                if block == 0 :
                    if self.y + j >= len(self.map) :
                        self.IS_MOVE = False

                    elif self.map[self.y + j][self.x + i] != 0 :
                        self.IS_MOVE = False

                    else : 
                        self.map[self.y + j][self.x + i] = block

                else :
                    self.map[self.y + j][self.x + i] = block

    def moveX(self, value) :
        if self.IS_MOVE :
            self.__init()
            self.x += value
        
        self.__draw()

    def moveY(self, value) :
        if self.IS_MOVE :
            self.__init()
            self.y += value

        self.__draw()

    def draw(self) :
        self.moveY(1)

        return self.IS_MOVE