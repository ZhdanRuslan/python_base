import logging
import os.path as path
from functools import lru_cache

logging.basicConfig(filename = path.join(path.dirname(__file__), "logfile.txt"),level=logging.INFO, format = u'%(levelname)-8s [%(asctime)s] %(message)s')

print(__file__)

@lru_cache(maxsize = 32)
def add (a, b):
    """Return the sum of a and b"""
    logging.info(str(a) + " + " + str(b) + " was called.")
    return a + b

@lru_cache(maxsize = 32)
def sub (a, b):
    """Return the sub of a and b"""
    logging.info(str(a) + " - " + str(b) + " was called.")
    return a - b

@lru_cache(maxsize = 32)
def mul (a, b):
    """Return the mul of a and b"""
    logging.info(str(a) + " * " + str(b) + " was called.")
    return a * b

@lru_cache(maxsize = 32)
def div (a, b):
    """Return the div of a and b"""
    if b == 0:
        logging.info("Dev by 0 was occured.")
        raise ZeroDivisionError
    else:
        logging.info(str(a) + " / " + str(b) + " was called.")
        return a / b

#switch operation
def switch_operation(arg, a_var, b_var):
    """Choose an operation which apply for a and b"""
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
    """Start point of a programm"""
    while True:
        try:
            action_var = input('Input an action e.q. "* / + - or stop" : ')
            if action_var.lower() == "stop":
                print("Bye!")
                break
            a_var = float(input('Input first operand: '))
            b_var = float(input('Input second operand: '))

        except ValueError as e:
            logging.info("Invalid value!")   
        try:
            print(switch_operation(action_var, a_var, b_var))
        except Exception as e:
            print("Somethings wrong!", e)

if __name__ == "__main__":
    main()