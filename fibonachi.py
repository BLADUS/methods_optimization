import OptimModule
from tabulate import tabulate

def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
        
def calculateFibonachiX(a, b, n, n1, n2):
    n=fib(n)
    n1=fib(n1)
    n2=fib(n2)
    x1 = a + (b-a)*(n/n2)
    x2 = a + (b-a)*(n1/n2)
    return x1, x2


expression = input("Введите математическое выражение (используйте 'x' как переменную): ")
a = input("Введите левую границу a: ")
b =  input("Введите правую границу b: ")
eps = input("Введите точность eps: ")
i=1

table = []  # Создаем пустую таблицу для хранения данных


while (b - a) / 2 > eps:
    x1, x2 = calculateFibonachiX(a, b, 6, 7, 8)
    f1, f2 = OptimModule.functions(expression, x1, x2)
    sr = ">" if f1 > f2 else "<"

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
print("x* =", xMin)
print("y* =",OptimModule.functions(expression, xMin))
