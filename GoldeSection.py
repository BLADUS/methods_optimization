import math

def calculateGoldenSectionX(a,b):
    x1 = a + ((3-math.sqrt(5))/2)*(b - a)
    x2 = a + (math.sqrt(5) - 1)*(b - a)
    return x1, x2