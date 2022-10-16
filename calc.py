import numpy as np

# валовый выпуск, изменения валового выпуска
def grossProd1 (EAmat,y):
    return EAmat.dot(y)

#  #валовый выпуск 2
# def grossProd2(xmat, y):
#     xprom = promProd(xmat)
#     return xprom + y

def checkX(x,a,y):
    return a.dot(x) + y

# межотраслевые потоки, изменения
def intersectoralFlows(a,x):
    res = np.empty((a.shape[0],a.shape[0]))
    for i in range(a.shape[0]):
        for j in range (a.shape[0]):
            res[i,j] = a[i,j] * x[j,0]
    return res

# перевод дельта у в стоимостное выражение
def convertFloat(y,dy):
    for i in range(y.shape[0]):
        dy[i,0] = (y[i,0]*dy[i,0])/100
    return dy

# затраты труда/опф
def laborOpfCosts(t, x):
    return np.multiply(t,x)

#промежуточный продукт
def promProd(xmat):
    xprom = np.empty((xmat.shape[0], 1))
    for i in range(xmat.shape[0]):
        sum = 0
        for j in range (xmat.shape[1]):
            sum += xmat[i, j]
        xprom[i,0] = sum
    return xprom

#материальные затраты
def matCosts(xmat):
    costs = np.empty((xmat.shape[0], 1))
    for j in range(xmat.shape[1]):
        sum = 0
        for i in range(xmat.shape[0]):
            sum += xmat[i, j]
        costs[j,0] = sum
    return costs

#условно-чистый продукт
def netProd(x,matcosts):
    return x-matcosts

# #прямые материальные затраты
# def dirMatCosts (xmat, x):
#     a = np.empty((xmat.shape[0], xmat.shape[1]))
#     for i in range(xmat.shape[0]):
#         for j in range(xmat.shape[1]):
#             a[i,j] = xmat[i,j] / x[j,0]
#     return a

#полные материальные затраты
def fullMatCosts (EAmat):
    e = np.eye(EAmat.shape[0])
    return EAmat - e

#косвенные материальные затраты
def indirMatCosts (a):
    return a.dot(a)

# # прямые затраты труда/ прямая фондоемкость
# def directCosts(xt, x):
#     t = []
#     for i in range(x.shape[0]):
#         t.append(xt[i,0]/x[i,0])
#     return t

# полная трудоемкость / полная фондоемкость
def fullCosts(t, a):
    EAmat = np.linalg.inv((np.eye(len(t))) - a)
    return np.dot(t,EAmat)

# дополнительная потребность в трудовых ресурсах / основных фондах
def addNeed(t, dx):
    dxt = np.empty((dx.shape[0],1))
    for i in range(len(t)):
        dxt[i,0] = t[i] * dx[i,0]
    return dxt


