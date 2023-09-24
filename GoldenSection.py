import math
import OptimModule
from tabulate import tabulate

def calculateGoldenSectionX(a,b):
    x1 = a + ((3 - math.sqrt(5)) / 2) * (b - a)
    x2 = a + b - x1
    return x1, x2

a = 1.5
b = 2
eps = 0.02
i=1

table = []  # Создаем пустую таблицу для хранения данных


while (b - a) / 2 > eps:
    x1, x2 = calculateGoldenSectionX(a, b)
    f1, f2 = OptimModule.functions(x1, x2)
    sr = "f(x1)>f(x2)" if f1 > f2 else "f(x1)<f(x2)"

    row = [i, a, b, (b - a) / 2, x1, x2, f1, f2, sr]
    table.append(row)

    if f1 > f2:
        a = x1
    else:
        b = x2

    i += 1

row = [i, a, b, (b - a) / 2]
table.append(row)

# Выводим таблицу
headers = ["Итерация", "a", "b", "(b-a)/2", "x1", "x2", "f(x1)", "f(x2)", "sr"]
print(tabulate(table, headers=headers, tablefmt="grid"))

xMin = (b+a)/2
print("x*=", xMin)
print("y*",OptimModule.functions(xMin))
