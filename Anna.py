import numpy as np
import numpy.linalg


def func():
    a = np.array([[0.3, 0.1, 0.4], [0.2, 0.3, 0.1], [0.2, 0.1, 0.2]], dtype=float)
    y = np.array([[30], [20], [80]])
    t = np.array([[2.5], [3.9], [1.1]], dtype=float)
    f = np.array([[0.8], [1.2], [1.5]], dtype=float)


    #   1) изменение валового выпуска и межотраслевых потоков
    #
    e = np.eye(3)
    e_a = e - a
    det_e_a = np.linalg.det(e_a)
    print("\nЗначение матрицы E-A\n", e_a)
    print("\n Определитель матрицы E-A:\n", det_e_a)

    e_a_inv = np.linalg.inv(e_a)
    print("\nЗначение обратной матрицы E-A:\n", e_a_inv)
    # объем валового продукта
    x = e_a_inv.dot(y)
    print("\nОбъем валового продукта по отраслям:\n", x)

    #     межотраслевые потоки

    xij = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=float)
    for i in 0, 1, 2:
        xij[i, 0] = a[i, 0] * x[0, 0]
        xij[i, 1] = a[i, 1] * x[1, 0]
        xij[i, 2] = a[i, 2] * x[2, 0]

    print("\nМежотраслевые потоки:\n", xij)

    # проверка
    r = a.dot(x)
    res = r + y
    print("\nПРОВЕРКА \n", res, "\n", x )
    #     стоймостное выражение для заданного процентного изменения конечного продукта

    _y1 = y[0, 0] * 20 / 100
    _y2 = y[1, 0] * 10 / 100
    _y3 = y[2, 0] * (-20) / 100
    _y = np.array([[_y1], [_y2], [_y3]])
    print(" \nИзменение конечного продукта:\n", _y)

    # изменения валового продукта

    _x = e_a_inv.dot(_y)
    print(" \nИзменение валового продукта:\n", _x)

    # изменения межотраслевых потоков

    _xij = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=float)
    for i in 0, 1, 2:
        _xij[i, 0] = a[i, 0] * _x[0, 0]
        _xij[i, 1] = a[i, 1] * _x[1, 0]
        _xij[i, 2] = a[i, 2] * _x[2, 0]

    print("\nИзменение межотраслевых потоков:\n", _xij)


    # 2) изменение потребности в трудовых ресурсах по отраслям

    _xt = np.array([[0], [0], [0]], dtype=float)

    for i in 0, 1, 2:
        _xt[i, 0] = t[i, 0] * _x[i, 0]

    print("\nИзменение потребности в трудовых ресурсах по отраслям:\n")
    print("1 отрасль:", _xt[0, 0])
    print("\n2 отрасль:", _xt[1, 0])
    print("\n3 отрасль:", _xt[2, 0])

    #     3)изменение потребности в основных производственных фондах по отраслям

    _f = np.array([[0], [0], [0]], dtype=float)
    for i in 0, 1, 2:
        _f[i, 0] = f[i, 0] * _x[i, 0]

    print("\nИзменение потребности в основных производственных фондах по отраслям:\n")
    print("1 отрасль:", _f[0, 0])
    print("\n2 отрасль:", _f[1, 0])
    print("\n3 отрасль:", _f[2, 0])

    #     4) промежуточный  продукт заданных отраслей

    x1j = 0
    x2j = 0
    x3j = 0
    for j in 0, 1, 2:
        x1j += xij[0, j]
        x2j += xij[1, j]
        x3j += xij[2, j]

    xjj = np.array([[x1j], [x2j], [x3j]], dtype=float)
    print("\nПромежуточный продукт заданных отраслей:\n")
    print("1 отрасль:", x1j)
    print("\n2 отрасль:", x2j)
    print("\n3 отрасль:", x3j)

    #     6)материальные затраты в каждую потребляющую отрасль

    xi1 = 0
    xi2 = 0
    xi3 = 0
    for i in 0, 1, 2:
        xi1 += xij[i, 0]
        xi2 += xij[i, 1]
        xi3 += xij[i, 2]

    xii = np.array([[xi1], [xi2], [xi3]], dtype=float)
    print("\nМатериальные затраты в каждую потребляющую область:\n")
    print("1 отрасль:", xi1)
    print("\n2 отрасль:", xi2)
    print("\n3 отрасль:", xi3)

    #     5)условно-чистый продукт
    z = x - xii
    print("\nУсловно-чистый продукт:\n", z)

    #   7)матрица коэф-в косвенных мат.затрат 1-го порядка

    a1 = numpy.linalg.matrix_power(a, 2)
    print("\nМатрица коэффициентов косвенных материальных затрат 1 -го порядка: \n", a1)

    #  8)затраты живого труда в каждой отрасли
    xt1 = t[0, 0] * x[0, 0]
    xt2 = t[1, 0] * x[1, 0]
    xt3 = t[2, 0] * x[2, 0]
    print("\nЗатраты живого труда:\n")
    print("1 отрасль:", xt1)
    print("\n2 отрасль:", xt2)
    print("\n3 отрасль:", xt3)


    #  9) затраты ОПФ
    bigf1 = f[0, 0] * x[0, 0]
    bigf2 = f[1, 0] * x[1, 0]
    bigf3 = f[2, 0] * x[2, 0]


    print("\nЗатраты ОПФ:\n")
    print("1 отрасль:", bigf1)
    print("\n2 отрасль:", bigf2)
    print("\n3 отрасль:", bigf3)

    #     10) матрица полных материальных затрат
    c = e_a_inv - e
    print("\nМатрица полных материальных затрат:\n", c)


func()
