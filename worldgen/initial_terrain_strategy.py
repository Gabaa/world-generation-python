import math
import random

from worldgen.terrain import Terrain


class InitialTerrainStrategy:
    def generate_initial_terrain(self):
        """
        Generates a new initial terrain after a reset.
        """

        pass


class PresetTriangleStrategy(InitialTerrainStrategy):
    def generate_initial_terrain(self):
        points = [(100, 398), (416, 250), (234, 133)]
        return Terrain(points)


class CircleBasedTriangleStrategy(InitialTerrainStrategy):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def generate_initial_terrain(self):
        angles = []

        for _ in range(3):
            deg = random.randrange(0, 360)
            rad = math.radians(deg)
            angles.append(rad)

        points = [(math.cos(rad), math.sin(rad)) for rad in angles]
        return Terrain(points)
