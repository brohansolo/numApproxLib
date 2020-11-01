################
### graph.py ###
################

import numpy as np
import matplotlib.pyplot as plt

def makegraph(function, legend):
    x = np.arange(-5, 5, 0.1)
    y = function(x)
    plt.plot(x, y, label = legend)


def showgraph(title, xaxis, yaxis, show_legend, minor_ticks):
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    if show_legend:
        plt.legend()
    if minor_ticks:
        plt.minorticks_on()
    plt.show()
    return

def errorgraph(function1, function2, legend):
    x = np.arange(-5, 5, 0.01)
    y1 = function1(x)
    y2 = function2(x)
    err = abs(y1-y2)
    plt.plot(x, err, label = legend)

 