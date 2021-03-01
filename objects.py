
import numpy as np

class Objects :
    def __init__(self, pg, screen, shape, color, chunk) :
        self.SHAPE = np.array(shape)
        self.COLOR = color
        self.CHUNK = chunk
        self.AMOUNT = np.unique(self.SHAPE, return_counts=True)[1][1]
        self.IS_MOVE = True

        self.x = 0
        self.y = 0
        self.pg = pg
        self.screen = screen

    def checkCrash(self) :
        for i in range(self.x, self.x + len(self.SHAPE[0]) * self.CHUNK[0], self.CHUNK[0]) :
            for j in range(self.y, self.y + len(self.SHAPE) * self.CHUNK[1], self.CHUNK[1]) :
                try :
                    if self.SHAPE[int((j - self.y) / self.CHUNK[1])][int((i - self.x) / self.CHUNK[0])] == 0 :
                        if tuple(self.screen.get_at((int(i + 1), int(j + 1))))[:-1] != (255, 255, 255)  :
                            self.IS_MOVE = False
                            
                            return True

                except :
                    self.IS_MOVE = False

                    return True

        return False

    def moveSide(self, value) :
        if self.IS_MOVE and self.x + value + self.CHUNK[0] * len(self.SHAPE[0]) < self.screen.get_width() and self.x + value > 0 :
            self.x += value

    def draw(self) :
        x = self.x
        y = self.y

        for line in self.SHAPE :
            for block in line :
                if block == 1 :
                    self.pg.draw.rect(
                        self.screen,
                        self.COLOR,
                        (x, y, self.CHUNK[0], self.CHUNK[1])
                    )

                x += self.CHUNK[0]
            
            x = self.x
            y += self.CHUNK[1]

        if self.IS_MOVE :
            self.y += 2