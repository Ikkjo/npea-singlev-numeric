import numpy as np
import numpy.linalg as lin

def parabola(f, x1, x3, tolerance):
    X = np.array([x1, (x1+x3)/2, x3]).transpose()
    const = np.ones(1, 3)
    Y = np.array([const, X, X * X]).transpose()

    fX = np.linspace(0, 0, len(X))
    for i in range(len(X)):
        fX[i] = f(X[i])

    abc = lin.solve(Y, f)

    x = -abc[1]/2/abc[2]
    fx = f(x)
    n = 0

    y_x = np.dot([1, x, x**2], abc)

    while abs(y_x - f(x)):
        break




















































    # X = np.array([x1, (x1 + x3) / 2, x3]).transpose()
    # pom = np.array([1, 1, 1]).transpose()
    # Y = np.array([pom, X, X * X]).transpose()
    # # x = [x1 x2 x3]' pom = [1 1 1]'
    # # Y = [1 1 1; x1 x2 x3; x1^2 x2^2 x3^2]
    # F = np.linspace(0, 0, len(X))
    # for i in range(0, len(X), 1):
    #     F[i] = f(X[i])
    #
    # abc = lin.solve(Y, F)
    #
    # x = -abc[1] / 2 / abc[2]
    # fx = f(x)
    # n = 0
    #
    # while np.abs(np.dot([1, x, x ** 2], abc) - fx) > tolerance:
    #     if (x > X[1]) and (x < X[2]):
    #         if (fx < F[1]) and (fx < F[2]):
    #             X = np.array([X[1], x, X[2]])
    #             F = np.array([F[1], fx, F[2]])
    #         elif (fx > F[1]) and (fx < F[2]):
    #             X = np.array([X[0], X[1], x])
    #             F = np.array([F[0], F[1], fx])
    #         else:
    #             print('Greska!')
    #     elif (x > X[0]) and (x < X[2]):
    #         if (fx < F[0]) and (fx < F[1]):
    #             X = np.array([X[0], x, X[2]])
    #             F = np.array([F[0], fx, F[2]])
    #         elif (fx > F[1]) and (fx < F[0]):
    #             X = np.array([x, X[1], X[2]])
    #             F = np.array([fx, F[1], F[2]])
    #         else:
    #             print('Greska!')
    #     else:
    #         print('x lezi van granica!')
    #
    #     pom = np.array([1, 1, 1]).transpose()
    #     Y = np.array([pom, X, X * X]).transpose()
    #     F = np.linspace(0, 0, len(X))
    #     for i in range(0, len(X), 1):
    #         F[i] = f(X[i])
    #
    #     abc = lin.solve(Y, F)
    #
    #     x = -abc[1] / 2 / abc[2]
        fx = f(x)
        n = n + 1

        return x, fx, n