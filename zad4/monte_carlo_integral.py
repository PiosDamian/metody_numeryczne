from random import random

from numpy.ma import arange, sqrt
from vpython import gcurve, color, graph, gdots, pi


def integral_function(x):
    return sqrt(1 - x ** 2)


def count_points(start, end):
    points = []
    max_y = float('-inf')
    for x in arange(start, end + 0.001, 0.1):
        y = integral_function(x)
        points.append((x, y))
        if y > max_y:
            max_y = y

    return {
        'points': points,
        'max_val': max_y
    }


def draw_x(move=-1, factor=2):
    return random() * factor + move


def average_sampling(start, end, n):
    result = 0
    points = []
    for i in range(1, n + 1):
        x = draw_x(start, end - start)
        y = integral_function(x)
        result = result + y
        points.append((x, y))
    return {
        'value': result * ((end-start)/n),
        'points': points
    }


def count_gross_field(a, b):
    return a * b


def draw_point(move_x=-1, factor_x=2, move_y=0, factor_y=1):
    return random() * factor_x + move_x, random() * factor_y + move_y


def draw_function_simple(start, end, tries=200):
    g = graph(title='Metoda prostego próbkowania')
    f1 = gcurve(graph=g, color=color.cyan)
    dots = gdots(graph=g, color=color.red)

    points = count_points(start, end)
    for point in points['points']:
        f1.plot(point)

    correct_points = 0

    for _ in range(0, tries):
        point = draw_point(start, end - start)
        dots.plot(point)
        if point[1] <= integral_function(point[0]):
            correct_points = correct_points + 1

    # max_val jest największą wartością funkcji,
    # odpowiada zmiennej H która musi być większa od f(x) dlatego koryguję o 0.1
    p_gross = count_gross_field(end - start, points['max_val'] + 0.0001)
    p = correct_points / tries * p_gross

    f1.label = '2 * wartość całki= ' + str(2 * p)
    dots.label = 'pole całkowite= ' + str(p_gross)


def draw_function_average(start, end, tries=200):
    g = graph(title='Metoda próbkowania średniej')
    f1 = gcurve(graph=g, color=color.cyan)
    dots = gdots(graph=g, color=color.red)

    points = count_points(start, end)
    for point in points['points']:
        f1.plot(point)

    sampling = average_sampling(start, end, tries)
    for point in sampling['points']:
        dots.plot(point)

    f1.label = '2 * wartość całki= ' + str(2 * sampling['value'])


if __name__ == '__main__':
    draw_function_simple(-1, 1)
    draw_function_average(-1, 1)
