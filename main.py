import pyglet
from pyglet.window import key
from pyglet.gl import *

from util.pyglethelper import draw_polygon
from terrain import Terrain


class Window(pyglet.window.Window):
    def __init__(self, terrain):
        super().__init__(width=500, height=500)
        self.terrain = terrain

    def on_draw(self):
        self.clear() 
        draw_polygon(*self.terrain.points)
        print('draw')
        print('\n'.join([f"{point}" for point in self.terrain.points]))

    def on_key_press(self, symbol, mod):
        if symbol == key.ESCAPE:
            self.close()
        elif symbol == key.SPACE:
            self.terrain.generate_additional_points()
        elif symbol == key.R:
            self.terrain.reset()

    def on_mouse_press(self, x, y, button, mod):
        print(f"Mouse pos: {x}, {y}")

    def run(self):
        pyglet.app.run()


def main():
    window = Window(Terrain())
    pyglet.app.run()


if __name__ == '__main__':
    main()
