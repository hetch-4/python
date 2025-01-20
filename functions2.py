i = 5
def f(arg = i):
    print(arg)

x = int(input("Enter value of x:")) 
f(x)

def f(a,L=[]):
    L.append(a)
    return L


#forms a list of the entered values
x = 0
y = int(input("enter number of inputs"))
print(y)
print("Enter value of input")
while x <= y:
    x = x + 1
    a = int(input("-:"))
    b = f(a)
print(b)

