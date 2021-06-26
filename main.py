from util.camera import Camera
import pyglet
from pyglet.window import key, mouse

from util.pyglethelper import draw_polygon
from worldgen import (CircleBasedTriangleStrategy, DistanceBasedOffsetStrategy,
                      ExponentialSplitsStrategy, LongestEdgeSplitStrategy, Terrain)


class Window(pyglet.window.Window):
    def __init__(self, terrain_gen_strategy, initial_terrain_strategy):
        super().__init__(width=500, height=500, caption="World Generation Tool", resizable=True)
        self.camera = Camera()
        self.terrain = initial_terrain_strategy.generate_initial_terrain(self.width, self.height)
        self.terrain_gen_strategy = terrain_gen_strategy
        self.initial_terrain_strategy = initial_terrain_strategy
        self.helper_labels = [
            pyglet.text.Label('[R]: Reset the current terrain', x=10, y=50),
            pyglet.text.Label('[Space]: Randomly mutate the terrain', x=10, y=30),
            pyglet.text.Label('[Esc]: Exit the program', x=10, y=10)
        ]

    def on_draw(self):
        self.clear()

        with self.camera:
            draw_polygon(*self.terrain.points)

        for label in self.helper_labels:
            label.draw()

    def on_key_press(self, symbol, mod):
        if symbol == key.ESCAPE:
            self.close()
        elif symbol == key.SPACE:
            self.terrain_gen_strategy.generate_points(self.terrain)
        elif symbol == key.R:
            self.terrain = self.initial_terrain_strategy.generate_initial_terrain(
                self.width, self.height)
            self.terrain_gen_strategy.on_reset()
            self.camera.position = 0, 0

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            self.camera.move(-dx, -dy)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.camera.zoom += scroll_y

    def run(self):
        pyglet.app.run()


def main():
    terrain_gen_strategy = ExponentialSplitsStrategy(
        LongestEdgeSplitStrategy(DistanceBasedOffsetStrategy()), 1)

    init_strategy = CircleBasedTriangleStrategy()

    window = Window(terrain_gen_strategy, init_strategy)
    window.run()


if __name__ == '__main__':
    main()
