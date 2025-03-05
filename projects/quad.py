#Solving a quadratic equation
import  math

print('in the form ax^2 + bx + c = 0\nInput')
#input coefficient
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

#calculate discriminant
dis = b**2 - 4*a*c
#check  if discriminant is -ve +ve or zero
if  dis > 0:
    root1 = (-b + math.sqrt(dis)) / (2*a)
    root2 = (-b + math.sqrt(dis)) / (2*a)
    print(f'root1: {root1}')
    print(f'root2: {root2}')
elif dis == 0:
    root = -b /(2*a)
    print(f'Root: {root}')
else:
    #complex roots
    real_part= -b / (2*a)
    imaginary_part = math.sqrt(abs(dis))/(2*a)
    print(f'root 1: {real_part} + {imaginary_part}i')
    print(f'root 2: {real_part} - {imaginary_part}i')