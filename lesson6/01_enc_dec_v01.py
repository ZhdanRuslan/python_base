def encrypt(in_a, in_b):
    if type(in_a) == int:
        print("Param A is ok")
    if str(in_b).isalpha():
        print("Param B is ok")
    result = list()
    for elem in in_b:
        symbol = ord(elem) 
        result.append(symbol ^ in_a)
    print(result)
    result.append(in_a)
    print(result)
    return ','.join(str(x) for x in result)

def decrypt(a):
    result = a.split(",")
    key = result[-1]
    del result[-1]
    print("result = ", result)
    print("key = ", key)
    result_str = ""
    for elem in result:
        z = int(elem) ^ int(key)
        result_str += str(chr(z))
    print(result_str)


decrypt(encrypt(44, "haha"))