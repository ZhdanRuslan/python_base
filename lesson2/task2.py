import math

try:
    radius = float(input("Input the radius "))
except ValueError:
    print("Wrong walue")
else:
    square = math.pi * radius**2
    print(square)