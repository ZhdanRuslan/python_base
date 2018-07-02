try:
    a = int(input("Type first integer value: "))
    b = int(input("Type second integer value: "))
    x = int(input("Type x: "))

except Exception as e:
    print(e)
else:
    print((x > a) & (x < b))
