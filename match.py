"""def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return 'Not found'
        case 418:
            return "I/'m a teapot"
        case _:
            return "Something/'s wrong with your internet "


#points x,y are on the x,y scale
x = int(input("x:"))
y = int(input("y:"))
point = (x,y)
def pt(point):
    match point:
        case (0,0):
            print("origin")
        case (0,y):
            print(f"Y={y}")
        case (x,0):
            print(f"X={x}")
        case (x,y):
            print(f"X={x},Y={y}")
        case _:
            raise ValueError("Not a point")

pt(point)"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point( x = 0, y = 0):
            print("origin")
        case Point( x = 0, y = y):
            print(f"Y = {y}")
        case Point( x = x , y = 0):
            print(f"X = {x}")
        case Point():
            print( " Somewhere else ")
        case _:
            print("not a point")

a = int(input("x:"))
b = int(input("Y:"))
g = Point( a , b)
where_is(g)