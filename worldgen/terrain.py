class Terrain:
    """
    Represents the generated terrain.
    """

    def __init__(self, points):
        self.points = list(points)
    
    def get_all_edges(self):
        n = len(self.points)
        for i in range(n):
            point_1 = self.points[i]
            point_2 = self.points[(i + 1) % n]
            yield point_1, point_2
