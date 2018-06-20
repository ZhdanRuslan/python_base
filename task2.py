#input side of triangle
import math

def calculate_triangle_aquare ():
    a = float(input("input side a: "))
    b = float(input("input side b: "))
    c = float(input("input side c: "))
    p = 0.5*(a+b+c)
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

print(calculate_triangle_aquare())