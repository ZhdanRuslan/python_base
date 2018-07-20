def favg(*varargs):
    return sum(varargs)/len(varargs)
r = range(50)
print(favg(*r))
print(favg(1, 2))