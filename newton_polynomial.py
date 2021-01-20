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


if __name__ == '__main__':
    draw_graph_newton()
