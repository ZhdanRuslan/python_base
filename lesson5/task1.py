import math

try:
    a = float(input("Input a: "))
    b = float(input("Input b: "))
except Exception as e:
    print("Wrong input!" + e)
else:
    def outer_function(a, b):
    
        def pow_side(x):
            return x*x

        return math.sqrt(pow_side(a) + pow_side(b))
    
print(outer_function(a,b))