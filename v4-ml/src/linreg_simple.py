from __future__ import print_function

import math
import numpy
import random
import matplotlib.pyplot as plt

def linear_regression(x, y):
    # TODO 1: implementirati linearnu regresiju

    slope = cov(x, y) / var(x)
    intercept = numpy.mean(y) - slope * numpy.mean(x)

    return slope, intercept


def predict(x, slope, intercept):
    # TODO 2: implementirati racunanje y na osnovu x i parametara linije

    return intercept + x * slope;


def create_line(x, slope, intercept):
    y = [predict(xx, slope, intercept) for xx in x]
    return y


def cov(x, y):
    result = ((x[i] - numpy.mean(x)) * (y[i] - numpy.mean(y)) for i in range(len(x)))
    return sum(list(result))


def var(x):
    result = (math.pow(x[i] - numpy.mean(x), 2) for i in range(len(x)))
    return sum(list(result))


if __name__ == '__main__':
    x = range(50)  # celobrojni interval [0,50]
    random.seed(1337)  # da rezultati mogu da se reprodukuju
    y = [(i + random.randint(-5, 5)) for i in x]  # y = x (+- nasumicni sum)

    slope, intercept = linear_regression(x, y)

    line_y = create_line(x, slope, intercept)

    plt.plot(x, y, '.')
    plt.plot(x, line_y, 'b')
    plt.title('Slope: {0}, intercept: {1}'.format(slope, intercept))
    plt.show()
