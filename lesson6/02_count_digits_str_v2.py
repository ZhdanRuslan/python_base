import re

def inserting_ind_into_str(input_string):
    result = ""
    for index, elem in enumerate(input_string):
        result += elem + str(index)
    return result

str_with_dig = inserting_ind_into_str("demo0234234234234 test")

print(str_with_dig)

res = re.findall("\d+", str_with_dig)

print(res)

for ind in res:
    print("{} - {}".format(ind, res.count(str(ind))))