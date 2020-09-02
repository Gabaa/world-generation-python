import math
import random

from worldgen.terrain import Terrain


class InitialTerrainStrategy:
    def generate_initial_terrain(self, width, height):
        """
        Generates a new initial terrain after a reset.
        """

        pass


class PresetTriangleStrategy(InitialTerrainStrategy):
    def generate_initial_terrain(self, width, height):
        points = [(100, 398), (416, 250), (234, 133)]
        return Terrain(points)


class CircleBasedTriangleStrategy(InitialTerrainStrategy):
    def generate_initial_terrain(self, width, height):
        angles = []

        for _ in range(3):
            deg = random.randrange(0, 360)
            rad = math.radians(deg)
            angles.append(rad)

        center = (width // 2, height // 2)
        circle_radius = min(width, height) // 4

        points = [(center[0] + int(math.cos(rad) * circle_radius),
                   center[1] + int(math.sin(rad) * circle_radius)) for rad in angles]
        return Terrain(points)
