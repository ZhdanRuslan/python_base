try:
    baseName = "Ruslan"
    inputName = str(input("Input name: "))
except Exception as e:
    print(e)
else:
    if baseName.lower() == inputName.lower():
        print("Names are equals")
    else:
        print("Not equals")1