from numpy.ma import arange
from vpython import gcurve, color

from integral_function import integral_function


def integral(start, end, n):
    return ((end - start) / (2 * n)) * multiple_summation(start, end, n)


def multiple_summation(start, end, n):
    result = 0
    for i in range(0, n):
        result = result + integral_function(start + i * ((end - start) / n)) + integral_function(
            start + (i + 1) * ((end - start) / n))
    return result


def draw_graph(start, end, n=10):
    f1 = gcurve(color=color.cyan)

    for i in arange(-1., 1.001, 0.01):
        x = round(i, 3)
        f1.plot(x, integral_function(x))

    f1.label = 'field = ' + str(2 * integral(start, end, n))


if __name__ == '__main__':
    draw_graph(-1, 1, 50)
