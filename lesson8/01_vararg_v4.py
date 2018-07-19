def favg(*varargs):
    result = []
    [result.append(elem) if type(elem)==int else result.append(e) for elem in varargs for e in elem]
    return result

#     high, low = [], []
# _Nones = [high.append(x) if is_condition_true() else low.append(x) for x in sequences]
                
x = [1,2,3,4]
print(favg(x,1,2,3,4,5,7))