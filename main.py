import pyglet
from pyglet.window import key

from util.pyglethelper import draw_polygon
from worldgen import (BetweenEachPointStrategy, DistanceBasedOffsetStrategy,
                      LongestEdgeSplitStrategy, Terrain, NSplitsStrategy)


class Window(pyglet.window.Window):
    def __init__(self, terrain, terrain_gen_strategy):
        super().__init__(width=500, height=500, resizable=True)
        self.terrain = terrain
        self.terrain_gen_strategy = terrain_gen_strategy

    def on_draw(self):
        self.clear()
        draw_polygon(*self.terrain.points)

    def on_key_press(self, symbol, mod):
        if symbol == key.ESCAPE:
            self.close()
        elif symbol == key.SPACE:
            self.terrain_gen_strategy.generate_points(self.terrain)
        elif symbol == key.R:
            self.terrain = create_terrain(3)

    def on_mouse_press(self, x, y, button, mod):
        print(f"Mouse pos: {x}, {y}")

    def run(self):
        pyglet.app.run()


def create_terrain(number_of_points):
    """
    Creates a new Terrain with random initial points.
    """

    if (3 > number_of_points):
        raise ValueError("Too low number of points, must have at least 3.")

    points = []
    points.append((100, 398))
    points.append((416, 250))
    points.append((234, 133))

    return Terrain(points)


def main():
    terrain = create_terrain(3)
    terrain_gen_strategy = LongestEdgeSplitStrategy(DistanceBasedOffsetStrategy())
    window = Window(terrain, NSplitsStrategy(terrain_gen_strategy, 50))
    window.run()


if __name__ == '__main__':
    main()
