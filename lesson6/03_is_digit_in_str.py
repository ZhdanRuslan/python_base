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

DATA = ["test string one", "ru2slan", "  left spaces",
"right spaces    ","   both side spaces   " ,"   both side spaces   "]

for i in DATA:
    print(inserting_ind_into_str(i))