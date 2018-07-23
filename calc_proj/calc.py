import logging
import os.path

logging.basicConfig(filename = os.path.join("calc_proj", "logfile.log"),level=logging.INFO, format = u'%(levelname)-8s [%(asctime)s] %(message)s')

def add (a, b):
    logging.info(str(a) + " + " + str(b) + " was called.")
    return a + b

def sub (a, b):
    logging.info(str(a) + " - " + str(b) + " was called.")
    return a - b

def mul (a, b):
    logging.info(str(a) + " * " + str(b) + " was called.")
    return a * b

def div (a, b):
    if b == 0:
        logging.info("Dev by 0 was occured.")
        raise ZeroDivisionError
    else:
        logging.info(str(a) + " / " + str(b) + " was called.")
        return a / b

#switch operation
def switch_operation(arg):
    if(arg=="*"):
        return mul(a_var, b_var)
    elif (arg=="/"):
        return div(a_var, b_var)
    elif (arg=="+"):
        return add(a_var, b_var)
    elif (arg=="-"):
        return sub(a_var, b_var)
    else:
        logging.info("Invalid arithmetic operator in input line!")
        raise Exception
def main():
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
            logging.info("Invalid value!")   
        try:
            print(switch_operation(action_var))
        except Exception as e:
            print("Somethings wrong!", e)

if __name__ == "__main__":
    main()