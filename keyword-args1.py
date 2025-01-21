def cheeseshop( kind, *arguments, **keywords):
    print("--do you have any", kind, "?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger","It,s very runny, sir.",
           "It's really very VERY runny, sir.",
           shopkeeper = "micheal palin",
           client = "John Cleese",
           sketch = "cheese Shop Sketch")