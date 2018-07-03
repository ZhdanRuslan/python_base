import math

width = int(input("Input width: "))
height = int(input("Input height: "))
simbol = input("Input simbol: ")

count = 0

for i in range(height):
    count +=1 
    for j in range (count):
        print(" ", end=" ")
    for k in range (width):
        print(simbol, end=" ")
    print()