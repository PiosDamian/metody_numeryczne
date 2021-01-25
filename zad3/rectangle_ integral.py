from numpy.ma import arange
from vpython import gcurve, color, graph

from integral_function import integral_function


def h_param(start, end, n):
    return (end - start) / n


def integral(start, end, n):
    return h_param(start, end, n) * multiple_summation(start, end, n)


def multiple_summation(start, end, n):
    result = 0
    h = h_param(start, end, n)
    for i in range(0, n):
        result = result + integral_function(start + (i + 0.5) * h)
    return result

def draw_graph(start, end, n=10):
    g = graph(title = 'Metoda prostokątów')
    f1 = gcurve(graph=g, color=color.cyan)

    for i in arange(start + 0.0, end + 0.001, 0.01):
        x = round(i, 3)
        f1.plot(x, integral_function(x))

    f1.label = 'field = ' + str(2 * integral(start, end, n))


if __name__ == '__main__':
    draw_graph(-1, 1, 50)
