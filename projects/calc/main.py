import math
def add(a,b):
    print( a +b)

def mult(a,b):
    print( a * b)

def divide(a,b):
    print(a/b)

def subtract(a,b):
    print( a - b)

operation =["+","-","*","/"]

a =int(input("enter first no"))
b = int(input("enter the second no"))

print(operation)
x = input("Choose your operation")
print(a,x,b,'=')


if x =="+":
    add(a,b)
elif x =="-":
    subtract(a,b)
elif x =="/":
    divide(a,b)
elif x == "*":
    mult(a,b)
else :
    print('Error, try Again')

print("^-^")    
