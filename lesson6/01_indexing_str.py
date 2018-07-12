def inserting_ind_into_str(input_string):
    if not input_string or type(input_string) != str:
        raise Exception
    result = ""
    for index in range(len(input_string)):
        result += input_string[index] + str(index)
    return result

DATA = ["test string one", "aubps", "alskjdhfjashfkdjashfkljhaskdfjhkjasdhf",
"aksdhkajsdhkjasdh","aksdjlkajsdlkjasdlkjas"]

for i in DATA:
    print(inserting_ind_into_str(i))