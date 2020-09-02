import pyglet
from pyglet.window import key

from util.pyglethelper import draw_polygon
from worldgen import (BetweenEachPointStrategy, CircleBasedTriangleStrategy,
                      DistanceBasedOffsetStrategy, ExponentialSplitsStrategy,
                      LongestEdgeSplitStrategy, NSplitsStrategy, PresetTriangleStrategy, Terrain)


class Window(pyglet.window.Window):
    def __init__(self, terrain_gen_strategy, initial_terrain_strategy):
        super().__init__(width=500, height=500, resizable=True)
        self.terrain = initial_terrain_strategy.generate_initial_terrain(self.width, self.height)
        self.terrain_gen_strategy = terrain_gen_strategy
        self.initial_terrain_strategy = initial_terrain_strategy

    def on_draw(self):
        self.clear()
        draw_polygon(*self.terrain.points)

    def on_key_press(self, symbol, mod):
        if symbol == key.ESCAPE:
            self.close()
        elif symbol == key.SPACE:
            self.terrain_gen_strategy.generate_points(self.terrain)
        elif symbol == key.R:
            self.terrain = self.initial_terrain_strategy.generate_initial_terrain(
                self.width, self.height)
            self.terrain_gen_strategy.on_reset()

    def on_mouse_press(self, x, y, button, mod):
        print(f"Mouse pos: {x}, {y}")

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
