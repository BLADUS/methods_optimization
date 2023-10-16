import math
import OptimModule
from tabulate import tabulate
import sympy as sp

expression = input("Введите математическое выражение (используйте 'x' как переменную): ")

derivative = OptimModule.derivative(expression)

print(derivative)

point = True
a = float(input("Введите левую границу a: "))
b =  float(input("Введите правую границу b: "))
eps = float(input("Введите точность eps: "))
#шаг n
n=1
while point:
    x = (a+b)/2
    f = OptimModule.functions(derivative, x)

    if abs(f) > eps:
        if f>0:
            b = x
        else:
            a=x
    else:
        point != point
