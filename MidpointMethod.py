import OptimModule
from tabulate import tabulate

expression = '-2.7**(-x/2)/2 - 3*x**2/2 + 2'

table = []

point = True
a = -2
b = 0
eps = 0.1
#шаг n
n=1
f = eps + 1

while abs(f) > eps:
    x = (a+b)/2
    f = OptimModule.functions(expression, x)
    
    if f > 0:
        b = x
        dif = '+'
    else: 
        a = x
        dif = '-'

    row = [n, a, b, x, f, dif]
    table.append(row)
    
    n+=1

headers = ['Итерация', 'a' , 'b', 'x', 'df(x)', 'Знак df(x)']
print(tabulate(table, headers=headers, tablefmt="grid"))

expression = '2.7**(-x/2)-x**3/2+2*x'
print("x*=", x)
print("y*",OptimModule.functions(expression,x))
