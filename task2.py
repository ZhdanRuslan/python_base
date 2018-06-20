import math

#calculate square of triangle
def calculate_triangle_aquare ():
    a = int(input("input side a: "))
    b = int(input("input side b: "))
    c = int(input("input side c: "))
    p = 0.5*(a+b+c)
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

print(calculate_triangle_aquare())