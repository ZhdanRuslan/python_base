def inserting_ind_into_str(input_string):
    if not input_string:
        raise Exception
    result = ""
    for index in range(len(input_string)):
        result += input_string[index] + str(index)
    return result

print(inserting_ind_into_str("asdasdasd"))