import math
import OptimModule
from tabulate import tabulate
import sympy as sp

def calculateXHord(a, b, f1, f2):
    return a - (f1/(f2-f1))*(b-a)

expression = '-2.7**(-x/2)/2 - 3*x**2/2 + 2'

a = -2
b = 0
eps = 0.05
i=1

data = []  # Создаем список данных для таблицы

f1, f2 = OptimModule.functions(expression, a, b)

point = True

while point:
    x = calculateXHord(a, b, f1, f2)
    fx = OptimModule.functions(expression, x)
    sign_fx = "+" if fx > 0 else "-" if fx < 0 else "0"

    # Добавляем данные в список
    data.append([i, a, b, x, fx, sign_fx])

    if abs(fx) < eps:
        point = False
    else:
        if fx > 0:
            b = x
        else:
            a = x
    i += 1

# Выводим таблицу в консоль с помощью tabulate
headers = ["n", "a", "b", "x", "fx", "знак fx"]
table = tabulate(data, headers, tablefmt="grid")
print(table)

expression = '2.7**(-x/2)-x**3/2+2*x'
print("x*=", x)
print("y*",OptimModule.functions(expression,x))
