from random import randrange, randint, random

from numpy.ma import arange
from vpython import graph, gcurve, gdots, color, sqrt, label


def draw_point():
    return random(), random()


def count():
    gd = graph(ymin=0, ymax=1.1, xmin=0, xmax=1.1)
    f1 = gcurve(graph=gd, color=color.cyan)
    f2 = gcurve(graph=gd, color=color.cyan)
    dots = gdots(graph=gd, color=color.red, radius=2)
    dots.plot(0.5, 0.5)
    for x in arange(0, 1.001, 0.01):
        f1.plot(x, circle_point_lower(x))
        f2.plot(x, circle_point_upper(x))

    points_count = randrange(200, 300)
    ok_points = 0
    while x <= points_count:
        x = x + 1
        point = draw_point()
        dots.plot(point[0], point[1])
        if circle_point_upper(point[0]) >= point[1] >= circle_point_lower(point[0]):
            ok_points = ok_points + 1

    field = ok_points / points_count
    pi = field / (0.5 ** 2)
    print(pi)


def circle_point_lower(x):
    return (1 - 2 * sqrt(x - x ** 2)) / 2


def circle_point_upper(x):
    return (2 * sqrt(x - x ** 2) + 1) / 2


if __name__ == '__main__':
    count()
