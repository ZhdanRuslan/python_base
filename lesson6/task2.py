def custom_length(string):
    n=0
    for i in string:
        if i != " ":
            n+=1
        continue
    return n

print(custom_length("zaz a z a"))