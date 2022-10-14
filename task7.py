"""
Решить систему диф уравнений хищник-жертва

1) x' = ax - bxy
2) y' = cxy - dy

Методом Рунге_кутты второго порядка точности
"""
import matplotlib.pyplot as plt
import numpy as np

a, b, c, d = 10, 2, 2, 10
x0, y0, t0 = 1, 1, 0
mint, maxt = 0, 3
alpha = 3./4.


def dif_x(x: float, y: float) -> float:
    res = float(a) * x - float(b) * x * y
    return res


def dif_y(x: float, y: float) -> float:
    res = float(c) * x - float(d) * x * y
    return res

def runge_kutta(m):
    """
    y_n+1 = y_n + h*((1-alpha)*f(x,y) + alpha*f(x+h/(2*alpha), y+f(x_n, y_n)*h/(2*alpha)))
    :return:
    """
    x, y = [x0], [y0]
    h = (maxt-mint)/m

    for i in range(m):
        x.append(x[i] + h * ((1 - alpha) * dif_x(x[i], y[i]) + alpha * dif_x(x[i] + h * dif_x(x[i], y[i]) / (2 * alpha),
                                                                             y[i] + h * dif_y(x[i], y[i]) / (2 * alpha))))
        y.append(y[i] + h * ((1 - alpha) * dif_y(x[i], y[i]) + alpha * dif_y(x[i] + h * dif_x(x[i], y[i]) / (2 * alpha),
                                                                             y[i] + h * dif_y(x[i], y[i]) / (2 * alpha))))

    return x, y


def run() -> None:
    N = 100
    results = runge_kutta(N)

    plt.title('phase trajectory')
    plt.plot(results[0], results[1], color='red')
    plt.legend('best')
    plt.savefig('task7_phase')

