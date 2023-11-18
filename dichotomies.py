import OptimModule
from tabulate import tabulate
import sympy as sp

def calculate_x(a,b,d):
    return (a+b-d)/2, (a+b+d)/2

expression = '2.7**(-x/2)-x**3/2+2*x'
a = -2
b = 0
eps = 0.1
d = 0.05
table = []  # Создаем пустую таблицу для хранения данных
i = 0

row = [i, a, b, (b-a)/2 ]
table.append(row)
i+=1

while (b-a)/2 > eps:
    x1, x2 = calculate_x(a,b,d)
    f1, f2 = OptimModule.functions(expression, x1, x2)

    if(f1>f2):
        a = x1
        sr = "f1>f2"
    else:
        b = x2 
        sr = "f1<f2"
    
    row = [i, a, b, x1, x2, f1, f2, sr,(b-a)/2 ]
    table.append(row)
    i+=1

headers = ["Итерация", 'a', 'b', 'x1', 'x2', 'f1', 'f2', 'f1vsf2', 'условие']
print(tabulate(table, headers=headers, tablefmt="grid"))

xMin = (b+a)/2
print("x* =", xMin)
print("y* =",OptimModule.functions(expression, xMin))


    
