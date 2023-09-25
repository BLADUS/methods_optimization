import math
from tabulate import tabulate
import sympy as sp


def functions(expression, *args):
    x = sp.symbols('x')
    f = sp.sympify(expression)
    
    if len(args) == 1:
        result = f.subs(x, args[0])
    elif len(args) == 2:
        result = (f.subs(x, args[0]), f.subs(x, args[1]))
    else:
        result = None  # Возвращаем None, если передано неверное количество аргументов
    
    return result


def comprision(f1,f2,arr,x1,x2):
    if f1>f2:
        arr[0]=x1
    else:
        arr[1]=x2

def check_unimodality(expression):
    x = sp.symbols('x')
    f = sp.sympify(expression)

    # Вычисляем первую и вторую производные
    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)

    return f_prime, f_double_prime




