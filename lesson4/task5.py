try:
    height = int(input("Input height: "))
except Exception as e:
    print("Wrong input: ")
else:
    for i in range(height):
        for j in range(i):
            if j == i - 1 or j == 0 or i == height - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()    



