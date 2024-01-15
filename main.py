from game_of_life import *

import goopylib as gp
from math import ceil

X = 0
Y = 0

CELL_SIZE = 10


class Cell(gp.Rectangle):
    instances = []

    def __init__(self, i, j):
        super().__init__((i * CELL_SIZE, j * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        Cell.instances.append(self)

        self.i = i
        self.j = j
        self.set_color("#181929")

    def update(self, state):
        self.hide(bool(state))

    @staticmethod
    def update_all(grid):
        for cell in Cell.instances:
            cell.update(grid[cell.i][cell.j])


def create_window(width, height):
    global X, Y

    win = gp.Window(width, height, "Conway's Game of Life in goopylib!")

    X = ceil(width / CELL_SIZE)
    Y = ceil(height / CELL_SIZE)

    camera = win.get_camera()
    camera.set_projection(0, 800, 0, 800)
    camera.move(-CELL_SIZE / 2, -CELL_SIZE / 2)

    background = gp.Rectangle((400, 400), 800, 800).draw(win)
    background.set_color("#45c3f5", "#fff", "#9d5fe8", "#5eccb4")

    [Cell(i, j).draw(win) for i in range(X) for j in range(Y)]
    return win


if __name__ == "__main__":
    window = create_window(800, 800)
    life.init(X, Y)
    
    # Add your own objects here
    life.spawn(GLIDER_GUN, 10, 10)
    life.spawn(GLIDER_GUN[::-1].T, 57, 10)

    while window.is_open():
        Cell.update_all(life.grid)
        life.update()
        gp.update()

    gp.terminate()
