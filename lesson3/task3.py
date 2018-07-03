print("Input the values: ")
try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    d = b * b - 4 * a * c
    print("D: " + str(d))

    #2,4,7
    if d < 0:
        print("d < 0")

    #1,6,9
    elif d == 0:
        # calculateZeroValue()
        print(-b / (2 * a))
    #2,4,-7
    else:
        # calculatePositive(d)
        print(-b + d / (2 * a))
        print(-b - d / (2 * a))

except Exception as e:
    print("Something wrong! Bye!" + e)

# else:
#     print('result for x1 = ' + x1)
#     print('result for x2 = ' + x2)

# def calculatePositive(d):
#     print(-b + d / (2 * a))
#     print(-b - d / (2 * a))

# def calculateZeroValue():
#     print(-b / (2 * a))