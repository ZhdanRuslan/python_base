barrier1 = int(input("Input i: "))

for i in range(barrier1):
    print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
