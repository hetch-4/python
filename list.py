def append_element(lst, element):
    lst.append(element)
    return lst

def reverse_list(lst):
    return lst[::-1]

def multiply_element(lst, factor):
    return [x * factor for x in lst]

def pipe(value, *functions):
    for func, *args in functions:
        if args:
            value = func(value, *args)
        else:
            value = func(value)
    return value

result = pipe([1, 2, 3], (append_element, 4), (reverse_list,), (multiply_element, 2))

print(result)