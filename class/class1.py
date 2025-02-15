class complex:
    # __init__ can have arguments for greater flexibility
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def f(self):
        return 'Hello world'
    
x = complex(3.0, -4.5)
print(x.r, x.i)


#there are only two kinds of valid attribute reference

# 1. data attributes
#They only spring to existance when first assigned to
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
    print(x.counter)
del x.counter

# 2. Method 
# a function that 'belongs to' an object
x.f()
xf = x.f
while True: 
    print(xf())
    #this prints till end of time ^_^
# x.f() === complex.f(x)

