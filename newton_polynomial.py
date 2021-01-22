from random import getrandbits

import numpy as np
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
    counter = 0

    # wyliczanie wartości funkcji podstawowej w tym przypadku cos(2*x) * exp(-0.2 * x)
    field_end = 8.05
    for x in arange(0, field_end, 0.1):  # x goes from 0 to 8
        # y = exp(-x) * cos(x)
        y = cos(2 * x) * exp(-0.2 * x)
        f1.plot(x, y)

        # losowanie punktów do wyliczania interpolacji - odbywa kiedy x znajduje się w przedziale 1..field_end-1
        if 1 < x <= field_end - 1 and counter % 2 == 0 and bool(getrandbits(1)):
            initial_points.append({'x': x, 'y': y})
            dots.plot(x, y)
        counter = counter + 1

    # wyliczanie i rysowanie interpolacji
    for point in newton_interpolation(initial_points, field_end):
        f2.plot(point['x'], point['y'])


# parametr field_end określa koniec dziedziny
def newton_interpolation(points, field_end):
    new_points = []
    # iteracja po x w zakresie 0..field_end z krokiem 0.1
    for i in arange(0, field_end, 0.1):
        x = round(i, 5)
        # wyliczanie y
        new_points.append({'x': x, 'y': multiple_summation(points, x)})
    return new_points


def multiple_summation(points, x):
    x_data = []  # pomocnicza tablica przechowująca współżędne x
    a_array = [] # tablica przechowująca an dla f(xi)
    for point in points:
        x_data.append(point['x'])
        a_array.append(point['y'])

    result = a_array[0] # a0
    # wielokrotne sumowanie po i 1..n
    # wewnątrz następuje wylicznie kolejnych stopni an dla f(xi...x1)
    for i in range(1, len(points)):
        a_array = an_array(x_data, a_array, i)
        print(a_array)
        result = result + a_array[0] * multiple_multiplication(points, x, i)
    return result


# wyliczanie kolejnych stopni an
# field - dziedzina
# a_table - aktualny stopień an
# level kolejny stopień an
# metoda opracowana na podstawie https://ece.uwaterloo.ca/~dwharder/aads/Algorithms/Newton_polynomials/
# wynikowa tablica jest używana jako tablica wejściowa w kolejny przejściu
# zaratość field dla każdego przejścia jest taka sama [x1...xn]
# przy każdym kolejnym wywołaniu zmienna level przyjmuje wyższą wartość
def an_array(field, a_table, level):
    result = []
    for index in range(0, len(a_table)-1):
        a_prev = a_table[index]
        a = a_table[index + 1]

        x_prev = field[index]
        x = field[index + level]

        result.append(an(a, a_prev, x, x_prev))

    return result


def an(t, prev_a, x, prev_x):
    return (t - prev_a) / (x - prev_x)


def multiple_multiplication(points, x, field_end):
    result = 1
    for index in range(0, field_end):
        xj = points[index]['x']
        result = result * (x - xj)
    return result


if __name__ == '__main__':
    draw_graph_newton()
