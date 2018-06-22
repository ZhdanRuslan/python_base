#listen input and check the number
import os
while True:
    print("Press Ctrl + C for stop...")
    try:
        a = float(input("input a number: "))
    except ValueError:
        print('Wrong input! Bye!')
        os._exit(0)
    if a%2==0:
        print(a**2)
    elif a%2 !=0:
        print(a*2)