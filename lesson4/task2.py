try:
    width = int(input("Input width: "))
    height = int(input("Input height: "))
    simbol = input("Input simbol: ")
except Exception as e:
    print("Something wrong " + e)

for i in range(height):
    for j in range (width):
        print(simbol, end=' ')
    print()