print("Input the values: ")
try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    x1 = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)

except Exception as e:
    print("Something wrong! Bye!" + e)

else:
    print('result for x1 = ', x1)
    print('result for x2 = ', x2)