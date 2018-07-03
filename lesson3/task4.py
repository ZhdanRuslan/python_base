

print("Input the values: ")
try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    def discriminant(a, b, c):
        result = b * b - 4 * a * c
        return result

    def calculatePositive():
        return [(-b + d / (2 * a)), (-b - d / (2 * a))]

    def calculateZero():
        return -b / (2 * a)

    d = discriminant(a, b, c)
    print(d)

    #2,4,7
    if d < 0:
        print("d < 0")
    #1,6,9
    elif d == 0:
        print(calculateZero())
    #2,4,-7
    else:
        print(calculatePositive())
        
except Exception as e:
    print("Something wrong! Bye!")