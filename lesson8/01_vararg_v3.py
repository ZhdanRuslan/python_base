def favg(*varargs):
    result = []
    [result.append(elem) for e in varargs if type(e) != int for elem in e]
    [result.append(e) for e in varargs if type(e) == int]
    return sum(result)/len(result)
                
x = [1,2,3,4]
print(favg(x,1,2,3,4,5,7))