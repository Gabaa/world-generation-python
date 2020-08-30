from util.mathhelp import euclidean_dist


class TerrainGenerationStrategy:
    def generate_points(self, terrain):
        """
        Generates one or more points, and adds them to the provided terrain.
        """

        pass


class BetweenEachPointStrategy(TerrainGenerationStrategy):
    def __init__(self, point_gen_strategy):
        self.point_gen_strategy = point_gen_strategy

    def generate_points(self, terrain):
        new_points = []

        for point_1, point_2 in terrain.get_all_edges():
            new_point = self.point_gen_strategy.generate_point(point_1, point_2)
            new_points += [point_1, new_point]

        terrain.points = new_points


class LongestEdgeSplitStrategy(TerrainGenerationStrategy):
    def __init__(self, point_gen_strategy):
        self.point_gen_strategy = point_gen_strategy

    def generate_points(self, terrain):
        new_points = []
        longest_edge_length = 0
        longest_edge_index = -1

        for i, (point_1, point_2) in enumerate(terrain.get_all_edges()):
            x1, y1 = point_1
            x2, y2 = point_2

            dist = euclidean_dist(x1, y1, x2, y2)
            if (dist > longest_edge_length):
                longest_edge_length = dist
                longest_edge_index = i

        for i, (point_1, point_2) in enumerate(terrain.get_all_edges()):
            new_points += [point_1]
            if (i == longest_edge_index):
                new_point = self.point_gen_strategy.generate_point(point_1, point_2)
                new_points += [new_point]

        terrain.points = new_points


class NSplitsStrategy(TerrainGenerationStrategy):
    def __init__(self, terrain_gen_strategy, n):
        self.terrain_gen_strategy = terrain_gen_strategy
        self.n = n

    def generate_points(self, terrain):
        for _ in range(self.n):
            self.terrain_gen_strategy.generate_points(terrain)
