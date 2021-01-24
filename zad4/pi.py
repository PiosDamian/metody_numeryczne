from random import randrange, randint, random

from numpy.ma import arange
from vpython import graph, gcurve, gdots, color, sqrt, label


def draw_point(factor=1):
    return random() * factor, random() * factor


def count():
    # algroytm działa także dla innych wielkości kwadratu r=a/2
    r = 0.5
    gd = graph(ymin=0, ymax=2 * r + 0.5, xmin=0, xmax=2 * r + 0.5)
    f1 = gcurve(graph=gd, color=color.cyan)
    f2 = gcurve(graph=gd, color=color.cyan)
    dots = gdots(graph=gd, color=color.red, radius=2)

    for x in arange(0, 2 * r + 0.001, 0.01):
        f1.plot(x, circle_point_lower(x, r))
        f2.plot(x, circle_point_upper(x, r))

    points_count = randrange(200, 300)
    ok_points = 0
    while x <= points_count:
        x = x + 1
        point = draw_point(2 * r)
        dots.plot(point[0], point[1])
        if circle_point_upper(point[0], r) >= point[1] >= circle_point_lower(point[0], r):
            ok_points = ok_points + 1

    field = ok_points / points_count
    pi = field / (r ** 2)
    f1.label = 'pi = ' + str(pi)
    f2.label = 'field = ' + str(field)
    gd.height = 450
    gd.width = 450


def circle_point_lower(x, r):
    return r - sqrt(2 * r * x - x ** 2)


def circle_point_upper(x, r):
    return sqrt(2 * r * x - x ** 2) + r


if __name__ == '__main__':
    count()
