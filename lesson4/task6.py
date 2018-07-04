try:
    n1 = int(input("Input first digit: "))
    n2 = int(input("Input last digit: ")) 
except Exception as exc:
    print("Wrong input! Bye!")
else:
    while n1 >= n2:
        print("n1 >= n2. Try again")
        n1 = int(input("Input first digit: "))
        n2 = int(input("Input last digit: "))
    else:
        sum=0
    for n1 in range(n1, n2+1):
        sum=n1+sum
    print(sum) 
    