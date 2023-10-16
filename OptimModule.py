import math
from tabulate import tabulate
import sympy as sp
import re


def functions(expression, *args):
    x = sp.symbols('x')
    f = sp.sympify(expression)
    
    # Замените символ "e" на число Эйлера
    f = f.replace(sp.E, sp.exp(1))
    
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

def derivative(expression):
    # Определите переменную символа 'x'
    x = sp.symbols('x')

    try:
        # Добавьте операторы умножения перед символами 'x'
        expression = re.sub(r'(?<=[0-9a-zA-Z)])x', r'*x', expression)
        # Замените неявные умножения на явные
        expression = expression.replace("^", "**")

        # Преобразуйте введенное выражение в символьное выражение
        f = sp.sympify(expression)

        # Вычислите производную
        derivative = sp.diff(f, x)

        # Представьте производную в нормальном виде
        normalized_derivative = sp.simplify(derivative)

        return normalized_derivative
    except sp.SympifyError:
        return "Ошибка ввода. Убедитесь, что введенное выражение корректно."




