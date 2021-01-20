from random import getrandbits

from numpy.ma import arange
from vpython import graph, color, gcurve, gdots, cos, exp


def draw_graph_newton():
    # przygotowanie wykresu
    gd = graph(title='Interpolacja Newtona\'a')
    f1 = gcurve(graph=gd, color=color.cyan)
    dots = gdots(graph=gd, color=color.red)
    f2 = gcurve(graph=gd, color=color.green)

    # tablica do przechowywania wylosowanych punktów
    initial_points = []

    # zmienna pomocnicza używana przy losowaniu punktów wielomianu
    index = 0

    # wyliczanie wartości funkcji podstawowej w tym przypadku cos(2*x) * exp(-0.2 * x)
    field_end = 8.05
    for x in arange(0, field_end, 0.1):  # x goes from 0 to 8
        y = exp(-x) * cos(x)
        f1.plot(x, y)

        # losowanie punktów do wyliczania interpolacji - odbywa kiedy x znajduje się w przedziale 1..field_end-1
        if 1 < x <= field_end - 1 and index % 2 == 0 and bool(getrandbits(1)):
            initial_points.append({'x': x, 'y': y})
            dots.plot(x, y)
        index = index + 1

    # wyliczanie i rysowanie interpolacji
    for point in newton_interpolation(initial_points, field_end):
        f2.plot(point['x'], point['y'])


def test():
    gd = graph(title='Interpolacja Newtona\'a')
    f1 = gcurve(graph=gd, color=color.cyan)
    dots = gdots(graph=gd, color=color.red)
    f2 = gcurve(graph=gd, color=color.green)

    points = [{'x': 1, 'y': 0.5}, {'x': 1.1, 'y': 0.6}, {'x': 1.2, 'y': 0.3}]
    f1.plot(0.7, .6)
    for point in points:
        f1.plot(point['x'], point['y'])
        dots.plot(point['x'], point['y'])
    f1.plot(1.3, 0.2)
    interpolation = newton_interpolation(points, 1.4)
    for point in interpolation:
        f2.plot(point['x'], point['y'])
    print(interpolation)


def newton_interpolation(points, field_end):
    new_points = []
    for i in arange(0, field_end, 0.1):
        x = round(i, 5)
        new_points.append({'x': x, 'y': multiple_summation(points)})
    return new_points


def multiple_summation(points):
    result = points[0]['y']
    for index in range(1, len(points)):
        point = points[index]
        result = result + point['y'] * multiple_multiplication(points, point['x'], index)
    return result


def multiple_multiplication(points, x, field_end):
    result = 1
    for index in range(0, field_end - 1):
        xj = points[index]['x']
        result = result * (x - xj)
    return result


if __name__ == '__main__':
    # draw_graph_newton()
    test()
