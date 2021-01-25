from numpy.ma import arange
from vpython import gcurve, color, graph

from integral_function import integral_function


def h_param(start, end, n):
    return (end - start) / n


def integral(start, end, n):
    return (h_param(start, end, n) / 6) * (
                integral_function(start) + 4 * multiple_summation_a(start, end, n) + 2 * multiple_summation_b(start,
                                                                                                               end, n))


def multiple_summation_a(start, end, n):
    result = 0
    h = h_param(start, end, n)
    for i in range(0, n):
        result = result + integral_function(start + i * h + h / 2)
    return result


def multiple_summation_b(start, end, n):
    result = 0
    h = h_param(start, end, n)
    for i in range(0, n):
        result = result + integral_function(start + i * h) + integral_function(end)
    return result


def draw_graph(start, end, n=10):
    f1 = gcurve(graph=graph(title='Metoda Simpsona'), color=color.cyan)

    for i in arange(start, end + 0.001, 0.01):
        x = round(i, 3)
        f1.plot(x, integral_function(x))

    f1.label = 'field = ' + str(2 * integral(start, end, n))


if __name__ == '__main__':
    draw_graph(-1, 1, 50)
