def ord(s):
    if s == "ё":
        return 1077.5
    else:
        return __builtins__.ord(s)

text = "фбвгдеёжзяa"
sorted_result = sorted(text, key=ord)

print(sorted_result)