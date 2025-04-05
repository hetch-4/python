def add_key(d, key_value):
    key, value = key_value
    d[key] = value
    return d

def increment_values(d, inc):
    return {k: v + inc for k, v in d.items()}

def filter_by_value(d, threshold):
    return {k: v for k,v in d.items() if v > threshold}

def pipe(value, *functions):
    for func, arg in functions:
        value = func(value, arg)
    return value

result = pipe({'a':1,'b':2}, (add_key, ('c',3)),(increment_values, 1), (filter_by_value, 2))
print(result)