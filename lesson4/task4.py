try:
    n1 = int(input("Input a: "))
    n2 = int(input("Input b: "))

    sum = (n2*(n2+1))/2-((n1-1)*((n1-1)+1))/2
except Exception as e:
    print("Erreor!" + e)
else:
    print(sum)