import numpy as np
from matplotlib import pyplot as plt


def Spiral():

    omega = 2

    t = np.linspace(0, 10, 1000)

    X = t * np.cos(omega * t)
    Y = t * np.sin(omega * t)

    plt.plot(X,Y)
    plt.grid(True)
    plt.show()

    return [X, Y]

Spiral()