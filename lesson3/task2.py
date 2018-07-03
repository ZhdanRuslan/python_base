import math

try:
    x = float(input("Input X: "))
except Exception as e:
    print("Something wrong. " + e)
else:
    if x >= -math.pi and x <= math.pi:
        print(math.cos(3*x))
    else:
        print(x) 