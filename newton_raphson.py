import numpy as np
from matplotlib import pyplot as plt

def newton_raphson(df, ddf, x0, tolerance=10**-(7), iter=100):
    x_prev = x0
    x_opt = np.inf
    finished_iter = True
    for i in range(iter):
        x_opt = x_prev - df(x_prev)/ddf(x_prev)
        if abs(x_opt - x_prev) < tolerance:
            finished_iter = False
            break

    return x_opt, finished_iter

