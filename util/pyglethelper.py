import pyglet
from pyglet.gl import *


def draw_line(start, end):
    x0, y0 = start
    x1, y1 = end

    pyglet.graphics.draw(
        2,
        GL_LINES,
        ("v2i", (x0, y0, x1, y1))
    )


def draw_polygon(*points):
    n = len(points)

    points = [v for point in points for v in point]

    indices = []
    for i in range(n):
        indices.append(i)
        indices.append((i + 1) % n)

    pyglet.graphics.draw_indexed(n, GL_LINES, indices, ("v2i", points))


def draw_square(x, y, w, h):
    x0, y0 = x, y
    x1, y1 = x+w, y+h
    
    pyglet.graphics.draw(
        4,
        GL_QUADS,
        ("v2i", (x0, y0, x0, y1, x1, y1, x1, y0))
    )
