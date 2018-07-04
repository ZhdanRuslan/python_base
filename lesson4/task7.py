try:
    n = int(input("Input digit: "))
except Exception as exc:
    print("Wrong input! Bye!")
else:
    while n < 0:
        print("n > 0. Try again")
        n = int(input("Input digit: "))
    else:
        fac = 1 
        i = 0 
        while i < n:
            i += 1
            fac = fac * i 
        print ("Factorial: " + str(fac))