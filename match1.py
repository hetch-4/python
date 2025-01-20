class Point:
    __match_args__ = ('x' , 'y')
    def __init__(self,x,y):
        self.x = x
        self.y = y

def p_is(point):
    match point:
        case [ ]:
            print("No points")
        case [Point(0,0)]:
            print("The origin")
        case [Point( x , y )]:
            print(f"Single point{x},{y}")
        case [Point( 0, y1), Point(0,y2)]:
            print(f"Two on the y axis at {y1}, {y2}")
        case _:
            print("something else")


