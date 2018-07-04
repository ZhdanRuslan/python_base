try:
    n = 0
    while n < 10:
        name = str(input("Input name: "))
        for z in name:
            n += 1
        if n < 10:
            print("Name too short")
        if any(map(str.isdigit, name)):
            print("Name have some digits")
    print("Everething OK")

except Exception as e:
    print("Something wrong!" + e)    