class my_class:
    # A simple example of class
    
    #classes allow two kinds of operations
    # 1. attribute refference
    i = 39872

    # 2. instantation
    def f(self):
        return 'Hello world'
    
     # __init__() rep newly created class instance
    def __init__(self):
        #creates an empty object
        self.data = []

print(my_class.i)

x = my_class()