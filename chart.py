import numpy as np
from random import randint


class Chart(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.__matrix = np.ndarray((width, height), dtype='S1')
        self.__matrix[:] = 'x'

    def _update(self):
        rand_x = randint(0, self._width - 1)
        rand_y = randint(0, self._height - 1)
        self.__matrix[rand_x, rand_y] = '-'

    @property
    def matrix(self):
        self._update()
        return self.__matrix