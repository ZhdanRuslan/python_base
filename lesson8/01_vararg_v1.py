def favg(*varargs):
    cust_sum = 0
    cust_len = 0
    for elems in varargs:
        if type(elems) != int:
            for elem in elems:
                cust_sum += elem
                cust_len += 1
        else:
            cust_sum += elems
            cust_len += 1
    return cust_sum/cust_len

print(favg([i for i in range(10)]))
print(favg(1,2,3,4))