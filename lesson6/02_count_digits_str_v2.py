import re

def inserting_ind_into_str(input_string):
    result = ""
    for index, elem in enumerate(input_string):
        result += elem + str(index)
    return result

str_with_dig = inserting_ind_into_str("demo test")

res = re.findall("\d+", str_with_dig)
print(str_with_dig)

for ind in range(len(res)):
    print("{}-{}".format(ind, res.count(str(ind))))