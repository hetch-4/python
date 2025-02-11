class point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case (0,0):
            print("Origin")
        case (0, y):
            print(f'Y={y}')
        case (x, 0):
            print(f'X = {x}')
        case (x,y):
            print(f'X = {x}, Y = {y}')
        case _:
            raise ValueError("Not a point")
        
#x, y = map(int, input("Enter point(x, y):").split())
#point0 = (x, y)
#print(point0)
#where_is(point0)
print(point)