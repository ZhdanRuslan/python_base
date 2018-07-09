# simply console calculator

def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b

#switch operation
def switch_operation(arg):
    if(arg=="*"):
        return mul(a_var, b_var)
    elif (arg=="/"):
        if b_var == 0:
            raise ZeroDivisionError
        else:
            return div(a_var, b_var)
    elif (arg=="+"):
        return add(a_var, b_var)
    elif (arg=="-"):
        return sub(a_var, b_var)
    else:
        raise Exception

action_var = ""
while True:
    try:
        action_var=""
        action_var = input('Input an action e.q. "* / + - or stop" : ')
        if action_var.lower() == "stop":
            print("Bye!")
            break
        a_var = float(input('Input first operand: '))
        b_var = float(input('Input second operand: '))

    except ValueError as e:
        print("Invalid value! Try again!")    
    try:
        print(switch_operation(action_var))
    except Exception as e:
        print("Somethings wrong!", e)