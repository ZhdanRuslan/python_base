import math

width = int(input("Input width: "))
height = int(input("Input height: "))
simbol = input("Input simbol: ")

count = 0

mid = int(width/2)
leftSide = int(width/2-1)
rightSide = int(width/2+1)

for i in range(height):
    
    
    for j in range (leftSide):
        print(" ", end=" ")
    for k in range (mid):
        print(simbol, end=" ")
    for q in range (rightSide):
        print(" ", end=" ")
    
    count += 1
    rightSide -= 1
    leftSide -=1 
    print()