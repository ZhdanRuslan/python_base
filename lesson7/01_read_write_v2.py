import os.path

def inserting_ind_into_str(input_string):
    if have_some_digits(input_string):
        return None
    input_string = input_string.strip()
    result = ""
    for index, elem in enumerate(input_string):
        result += elem + str(index)
    return result

def have_some_digits(input_string):
    return any(map(str.isdigit, input_string))

with open(os.path.join("lesson7", "result.ind"), "w") as result_file:
    with open(os.path.join("lesson7", "input.txt")) as input_file:
        for line in input_file:
            result_file.write(str(inserting_ind_into_str(line)))