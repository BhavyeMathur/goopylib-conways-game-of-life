import numpy as np
from scipy.signal import convolve2d


kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])
grid: np.array


def update():
    global grid
    neighbours = convolve2d(grid, kernel, mode="same")

    # grid is an NxM matrix of alive (1) or dead (0) cells
    # neighbours is an NxM matrix of number of alive neighbouring cells
    # neighbours contains values from 0 to 8 (0000 to 1000 in binary)
    #
    # Conway's game of life rules:
    #   if (cell is alive) AND (neighbours is 2 or 3)
    #       alive
    #   elif (cell is dead) AND (neighbours is 3)
    #       alive
    #   else
    #       dead
    #
    # In Binary (least significant 4 bits are shown):
    #   if (cell is 0001) AND (neighbours is 0010 or 0011) OR
    #   if (cell is 0000) AND (neighbours is 0011)
    #       alive
    #   else
    #       dead
    #
    # So,
    #   if neighbours has 1 in any bit except least-significant 2: dead
    #   if neighbours has least-significant bits 11: alive
    #   if neighbours has least-significant bits 10 but cell has least-significant bits 01: alive
    #
    # Following from the above logic:
    #   if bitwise-or(neighbours, cell) has least-significant bits 11 and other bits 0: alive
    #   else: dead
    #
    # Finally, alive = (bitwise-or(neighbours, cell) == 0000 00011)

    grid = (neighbours | grid) == 3


def spawn(structure, x, y):
    n, m = structure.shape
    grid[x:x + m, y:y + n] = structure.T


def init(N, M):
    global grid
    grid = np.zeros((N, M)).astype(np.uint8)
