import numpy as np

def fibb(f, a, b, tolerance):
    n = 1

    while ((b - a)/ tolerance) > fib_num(n):
        n += 1

    x1 = a + (fib_num(n-2)/fib_num(n)) * (b - a)
    x2 = a + b - x1

    for i in range(2, n+1):
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        elif f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = a + b - x1

        else:  # f(x1) == f(x2)
            x1 = a + (fib_num(n-2)/fib_num(n)) * (b - a)
            x2 = a + b - x1

    x_opt = min(f(x1), f(x2))
    f_opt = f(x_opt)

    return f_opt, x_opt, n

def fib_num(n):
    if n < 3:
        f_n = 1
    else:
        f_np = 1
        f_npp = 1
        for i in range(3, n+1):
            f_n = f_np + f_npp
            f_npp = f_np
            f_np = f_n

    return f_n