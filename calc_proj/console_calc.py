# simply console calculator
a_var = float(input('Input first operand: '))
action_var = input('Input an action e.q. "* / + -" : ')
b_var = float(input('Input second operand: '))

#switch operation
def switch_operation(arg):
    if(arg=="*"):
        return a_var * b_var
    elif (arg=="/"):
        return a_var / b_var
    elif (arg=="+"):
        return a_var + b_var
    elif (arg=="-"):
        return a_var - b_var
    else:
        print("wrong input")


print(switch_operation(action_var))