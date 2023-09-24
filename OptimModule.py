import math
from tabulate import tabulate


def functions(*x):
    if len(x)==2:
        x1, x2 = x
        return x1 - math.log(x1) + 5, x2 - math.log(x2) + 5
    else :
        xmin = x[0]
        return 3*xmin**4 + math.exp(-2*xmin) + 8,


def comprision(f1,f2,arr,x1,x2):
    if f1>f2:
        arr[0]=x1
    else:
        arr[1]=x2




