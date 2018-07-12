def outer_func():
    temp = None
    def func():
        x = int(input('Введите число >>> '))
        if x >= 0:
            nonlocal temp
            temp = x
            print(temp)
            func()
        else:
            print(temp)
            func()
    func()
outer_func()