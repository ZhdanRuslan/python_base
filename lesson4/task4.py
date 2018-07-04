try:
    n1 = int(input("Input a: "))
    n2 = int(input("Input b: "))

except Exception as e:
    print("Wrong input! Bye!")
else:
    while n1 >= n2:
        print("n1 >= n2. Try again")
        n1 = int(input("Input a: "))
        n2 = int(input("Input b: "))
    else:
        sum = (n2*(n2+1))/2-((n1-1)*((n1-1)+1))/2
        print(sum)