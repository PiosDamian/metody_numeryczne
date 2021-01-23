from vpython import gcurve, exp, color, cos, gdots, graph, pi

from numpy.ma import arange

from lagrange_polynomial import lagrange_interpolation
from newton_polynomial import newton_interpolation


def czybyszew_points(amount, field_start, field_end):
    result = []
    for i in range(0, amount + 1):
        result.append(czybyszew_point(i, amount, field_start, field_end))
    return result


def czybyszew_point(k, n, field_start, field_end):
    return (field_end - field_start) / 2 * cos(((2 * k + 1) * pi) / (2 * n + 2)) + (field_start + field_end) / 2


def origin_lagrange_function(x):
    # return cos(2 * x) * exp(-0.2 * x)
    return exp(-x) * cos(5 * x)


def lagrange_czybyszew(nodes_amount):
    gd = graph(title='Interpolacja Lagrange\'a')
    f1 = gcurve(graph=gd, color=color.cyan)
    dots = gdots(graph=gd, color=color.red)
    f2 = gcurve(graph=gd, color=color.green)

    # wyliczanie wartości funkcji podstawowej w tym przypadku cos(2*x) * exp(-0.2 * x)
    field_end = 6.05
    for x in arange(0, field_end, 0.1):
        y = origin_lagrange_function(x)
        f1.plot(x, y)

    # tablica do przechowywania wylosowanych punktów
    initial_points = []
    for x in czybyszew_points(16, 0, field_end):
        y = origin_lagrange_function(x)
        dots.plot(x, y)
        initial_points.append({'x': x, 'y': y})

    # wyliczanie i rysowanie interpolacji
    for point in lagrange_interpolation(initial_points, field_end):
        f2.plot(point['x'], point['y'])


def origin_newton_function(x):
    return exp(-x) * cos(5 * x)


def newton_czybyszew(nodes_amount):
    gd = graph(title='Interpolacja Newtona\'a')
    f1 = gcurve(graph=gd, color=color.cyan)
    dots = gdots(graph=gd, color=color.red)
    f2 = gcurve(graph=gd, color=color.green)

    # wyliczanie wartości funkcji podstawowej w tym przypadku cos(2*x) * exp(-0.2 * x)
    field_end = 8.05
    for x in arange(0, field_end, 0.1):
        y = origin_newton_function(x)
        f1.plot(x, y)

    # tablica do przechowywania wylosowanych punktów
    initial_points = []
    for x in czybyszew_points(nodes_amount, 0, field_end):
        y = origin_newton_function(x)
        dots.plot(x, y)
        initial_points.append({'x': x, 'y': y})

    # wyliczanie i rysowanie interpolacji
    for point in newton_interpolation(initial_points, field_end):
        f2.plot(point['x'], point['y'])


if __name__ == '__main__':
    lagrange_czybyszew(16)
    newton_czybyszew(16)
