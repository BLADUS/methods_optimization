import math
from tabulate import tabulate


def functions(*x):
    if len(x)==2:
        x1, x2 = x
        return 3*x1**4 + math.exp(-2*x1) + 8,3*x2**4 + math.exp(-2*x2) + 8
    else :
        xmin = x[0]
        return 3*xmin**4 + math.exp(-2*xmin) + 8,


def comprision(f1,f2,arr,x1,x2):
    if f1>f2:
        arr[0]=x1
    else:
        arr[1]=x2




