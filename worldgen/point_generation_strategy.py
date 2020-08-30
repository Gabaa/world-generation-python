import math
import random

from util.mathhelp import euclidean_dist


class PointGenerationStrategy:
    def generate_point(self, point_1, point_2):
        """
        Generates an intermediary point between two existing points.
        """

        pass


class DistanceBasedOffsetStrategy(PointGenerationStrategy):
    def generate_point(self, point_1, point_2):
        x1, y1 = point_1
        x2, y2 = point_2

        new_x = (x1 + x2) // 2
        new_y = (y1 + y2) // 2

        dist = int(euclidean_dist(x1, y1, x2, y2))
        offset = dist // 2
        new_x += random.randint(-offset, offset)
        new_y += random.randint(-offset, offset)

        return new_x, new_y
