def custom_func(a, b, c):
    return (a+b+c)/3

while True:
    try:
        print("Input any word for exit")
        num_one = float(input("Input the 1st digit: "))
        num_two = float(input("Input the 2nd digit: "))
        num_three = float(input("Input the 3rd digit: "))

        print(custom_func(num_one, num_two, num_three))
    except Exception:
        print("Good bye!")
        break
    