def chees(kind, *arguments, **keywords):
    print("--doyou have any", kind, "?")
    print("--I'm sorry, were are alll out of", kind)
    for arg in arguments:
        print(arg)
    print("-"* 40)
    for kw in keywords:
        print(kw, ':', keywords[kw])

# **keyword recieves a dictionary 
# *argument recieves a turple containing positional arguments
# *argument must come before the **keyword

chees("limburger","It's very runny, sir.",
      "it's really very, very runny, sir.",
      shopkeeper = "Micheal palin",
      client = "John Cleese",
      sketch = "cheese Shop sketch")