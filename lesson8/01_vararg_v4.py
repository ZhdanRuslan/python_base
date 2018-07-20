def favg(*varargs):
    result = []
    
    def flatten(nested):
        try:
            first, *rest = nested
        except TypeError:
            return [nested]
        except ValueError:
            return []
        return flatten(first) + flatten(rest)

    result = flatten(varargs)
    return sum(result)/len(result)


print(favg([1,2,3]))
print(favg(1, 2))
print(favg(x for x in range(50)))
print(favg([range(20)]))