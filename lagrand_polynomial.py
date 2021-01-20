from random import getrandbits

from numpy.ma import arange
from vpython import gcurve, exp, color, cos, gdots, graph, label

# ze względu na losowość punktów przekazanych do wyliczenie interpolacji, wykres interpolacyjny jest bardziej lub mniej dokładny

# główna funkcja
def draw_graph_lagrange():
    # przygotowanie wykresu
    gd = graph(title='Interpolacja Lagrand\'a')
    f1 = gcurve(graph=gd, color=color.cyan)  # a graphics curve
    dots = gdots(graph=gd, color=color.red)
    f2 = gcurve(graph=gd, color=color.green)

    # tablica do przechowywania wylosowanych punktów
    initial_points = []

    # zmienna pomocnicza używana przy losowaniu punktów wielomianu
    index = 0

    # wyliczanie wartości funkcji podstawowej w tym przypadku cos(2*x) * exp(-0.2 * x)
    field_end = 8.05
    for x in arange(0, field_end, 0.1):  # x goes from 0 to 8
        y = cos(2 * x) * exp(-0.2 * x)
        f1.plot(x, y)

        #losowanie punktów do wyliczania interpolacji - odbywa kiedy x znajduje się w przedziale 1..field_end-1
        if 1 < x <= field_end - 1 and index % 2 == 0 and bool(getrandbits(1)):
            initial_points.append({'x': x, 'y': y})
            dots.plot(x, y)
        index = index + 1

    # wyliczanie i rysowanie interpolacji
    for point in lagrange_interpolation(initial_points, field_end):
        f2.plot(point['x'], point['y'])


# funkcja licząca wartości wielomiany w zakresie 0..field_end
def lagrange_interpolation(points, field_end):
    new_points = []
    for i in arange(0, field_end, 0.1):
        x = round(i, 5)
        new_points.append({'x': x, 'y': multiple_summation(points, x)})
    return new_points


# wielokrotne mnożenie z pominięciem xi=xj, przyrównywanie na podstawie wartości, nie indeksu
# funkcja używana zarówno do oblicznia licznika jak i mianownika
def multiple_multiplication(points, x, xi):
    result = 1
    for point in points:
        xj = point['x']
        if xj == xi:
            continue
        result = result * (x - xj)
    return result


# wielokrotne sumowanie wraz z mnożeniem przez wartośc funkcji postawowej
def multiple_summation(points, f_param):
    result = 0
    for point in points:
        result = result + point['y'] * (
                multiple_multiplication(points, f_param, point['x']) / multiple_multiplication(points, point['x'],
                                                                                               point['x']))
    return result


if __name__ == '__main__':
    draw_graph_lagrange()
