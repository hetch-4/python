import math
print(f'The value of pi is approximately {math.pi:.3f}')
# above prints pi to 3 decimal places

table = {'Sjoerd': 4127, 'Jack':4038, 'Dcab':  7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}') 
    # : will cause the a min number of characters wide

animals = 'eels'
print(f'my hovercraft is full of {animals!s}')
    #  ! convert the value before it is formated
    # !a applies ascii(), !s - str(), !r - repr()

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
# = can be used to expand an expression 
# eg {bugs=}  output --> bugs='roaches'
