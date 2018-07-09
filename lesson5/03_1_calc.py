command = ""
result = ""
while True:
    command = input("Input expression or exit: ")
    if command.lower() == "exit":
        break
    try:
        print(eval(command))
    except Exception as e:
        print("Invalid expression", e)
    