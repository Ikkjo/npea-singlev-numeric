import numpy as np

def secant(df, x1, x0, tolerance, iter):
    x_new = x1
    x_prev = x0
    x_pre_prev = np.inf
    it = 0
    while abs(x_new - x_prev) > tolerance or it <= iter:
        x_pre_prev = x_prev
        x_prev = x_new
        x_new = x_new - df(x_new) * (x_new - x_prev) / (df(x_new) - df(x_pre_prev))

        it += 1

    x_opt = x_new
    return x_opt, it