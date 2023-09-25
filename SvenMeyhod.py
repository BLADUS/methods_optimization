import math
import OptimModule
from tabulate import tabulate

def calculateXnAscend(n, xn, h):
    return xn + (2**n)*h

def calculateXnDescend(n, xn, h):
    return xn - (2**n)*h

#expression = input("Введите математическое выражение (используйте 'x' как переменную): ")

#f_prime, f_double_prime = OptimModule.check_unimodality(expression)

#print("Первая производная:", f_prime)
#print("Вторая производная:", f_double_prime)

expression = 'x**3 + 0.2*cos(5*x)'

n = 0
h = float(input("Введите шаг:"))
xn = float(input("Введите x0:"))

print("n\t\txn\t\tf(xn)")  # Заголовки столбцов

while n < 10:
    fxn = OptimModule.functions(expression, xn)
    print("{}\t\t{:.4f}\t\t{:.4f}".format(n, xn, fxn))
    xn = calculateXnAscend(n, xn, h)
    n += 1


