import os.path

def inserting_ind_into_str(input_string):
    if not input_string or type(input_string) != str:
        raise Exception
    if is_digit_present(input_string) == None:
        return None
    if input_string.startswith(" "):
        input_string = input_string.lstrip()
    elif input_string.endswith(" "):
        input_string = input_string.rstrip()
    
    result = ""
    for index in range(len(input_string)):
        result += input_string[index] + str(index)
    return result

# Check digit in string
def is_digit_present(input_string):
    if not input_string or type(input_string) != str:
        raise Exception
    for elem in input_string:
        if elem.isdigit():
            return None
    else:
        return input_string

result_str = ""

with open(os.path.join("lesson7", "result.ind"), "w") as result_file:
    with open(os.path.join("lesson7", "input.txt")) as input_file:
        for line in input_file:
            result_file.write(str(inserting_ind_into_str(line)))