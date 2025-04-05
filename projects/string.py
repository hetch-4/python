#String Manipulation Pipeline

def append_text(text, suffix):
    return text + suffix

def replace_characters(text, old, new):
    return text.replace(old, new)

def pipe(value, *functions):
    for func, *args in functions:
        value = func(value, *args)
    return value

# Example
result = pipe("hello", (append_text, " world"), (replace_characters, "world","python"))

print(result)