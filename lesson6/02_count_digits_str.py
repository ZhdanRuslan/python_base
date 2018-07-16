import re

def inserting_ind_into_str(input_string):
    def digit_counter(a):
        result_map = {}
        for elem in a:
            if elem.isdigit() and elem in result_map:
                result_map[elem] += 1
            elif elem.isdigit():
                result_map[elem] = 1
            else:
                continue
        return result_map

    if not input_string or type(input_string) != str:
        raise Exception
    result = ""
    for index in range(len(input_string)):
        if input_string[index] == " ":
            continue
        result += input_string[index] + str(index)
    return digit_counter(result)



r =inserting_ind_into_str("a222222sd")
print(r)
