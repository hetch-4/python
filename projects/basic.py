def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def subtract(a,b):
    return a-b

def pipe(value, *functions):
    for func, arg in functions:
        value = func(value, arg)
    return value

result = pipe(5, (add, 3), (multiply, 4), (subtract, 10))
print(result)