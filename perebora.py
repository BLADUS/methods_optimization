from tabulate import tabulate

table = []
point = True
i=-2
while point:
    f = 2.7**(-i/2)-(i**3/2)+2*i
    row = [i, f]
    table.append(row)
    i+=0.1
    if i>1:
        point = not True

headers = ['x', 'f(x)']
print(tabulate(table, headers=headers, tablefmt="grid"))