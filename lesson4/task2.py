width = int(input("Input width: "))
height = int(input("Input height: "))
simbol = input("Input simbol: ")

for i in range(width):
    for j in range (height):
        print(simbol, end=' ')
    print()