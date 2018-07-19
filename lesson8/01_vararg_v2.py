def favg(*varargs):
    result = []
    for sublist in varargs:
        if type(sublist) == int:
            result.append(sublist)
        else:
            for elem in sublist:
                result.append(elem)
    return sum(result)/len(result)
                
x = [1,2,3,4]
print(favg(x,1,2,3,4,5,7))