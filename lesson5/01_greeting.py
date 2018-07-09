def say_hello(name = "Ruslan"):
    return str.format("Hello {}", name)

try:
    input_name = str(input("Input the name: "))
except Exception as e:
    print("Programm has beet stopped, bye! Error was occured.", e)
else:
    #invocation without params
    print(say_hello())
    #invocation with params
    print(say_hello(input_name))



 