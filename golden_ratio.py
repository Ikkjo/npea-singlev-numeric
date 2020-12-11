import numpy as np

def golden_ratio(f, a, b, tolerance):

    c = (3 - np.sqrt(5)) / 2

    x1 = a + c * (b - a)
    x2 = a + b - x1
    iter = 1
    while abs(x1 - x2) > tolerance:
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        elif f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = a + b - x1

        else:  # f(x1) == f(x2)
            x1 = a + c * (b - a)
            x2 = a + b - x1

        iter += 1

    x_opt = min(f(x1), f(x2))
    f_opt = f(x_opt)

    return f_opt, x_opt, iter