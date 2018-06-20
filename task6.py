#listen input and check the number
while True:
    print("Press Ctrl + C for stop...")
    a = float(input("input a number: "))
    if a%2==0:
        print(a**2)
    elif a%2 !=0:
        print(a*2)
    else:
        print("Something wrong!")