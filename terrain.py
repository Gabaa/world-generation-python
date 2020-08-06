import random
import math


class Terrain:
    """
    Represents the generated terrain.
    """

    def __init__(self):
        self.points = []

        self.reset()

    def reset(self):
        """
        Generate the initial list of points in the terrain.
        """
        self.points = []
        self.points.append((100, 398))
        self.points.append((416, 250))
        self.points.append((234, 133))

    def generate_additional_points(self):
        """
        Generate a point between each existing point, slightly offset.
        """

        n = len(self.points)

        new_points = []

        for i in range(n):
            point_1 = self.points[i]
            point_2 = self.points[(i + 1) % len(self.points)]

            new_point = self.generate_point(point_1, point_2)

            new_points += [point_1, new_point]
        
        self.points = new_points


    @staticmethod
    def generate_point(point_1, point_2) -> "Tuple[int, int]":
        x1, y1 = point_1
        x2, y2 = point_2

        new_x = (x1 + x2) // 2
        new_y = (y1 + y2) // 2

        dist = int(math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2))
        offset = dist // 4
        new_x += random.randint(-offset, offset)
        new_y += random.randint(-offset, offset)

        return new_x, new_y
