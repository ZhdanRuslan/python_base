def outer_function(list):
    odd_list = []
    even_list = []

    for elem in list:
        if elem % 2 == 0:
            print(elem, "Even")
            even_list.append(elem)
        else:
            print(elem, "Odd")
            odd_list.append(elem)

        obj_list = {
        'odd' : odd_list,
        'even' : even_list
        }
    
    return obj_list

list = [2, 5, 7, 4]

print(outer_function(list))