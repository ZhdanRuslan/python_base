import re

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

str_with_dig = inserting_ind_into_str(" demo test    ")

res = re.findall("\d+", str(str_with_dig))
print(str_with_dig)

for ind in range(len(res)):
    print("{}-{}".format(ind, res.count(str(ind))))
