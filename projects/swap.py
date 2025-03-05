#swap two variables with no temp
#input two variables from user 
a = input("enter the value of the first variable:")
b = input("enter the value of the second variable:")

print(f'a:{a}\nb:{b}')

a, b = b, a
print('after swaping')
print(f'a:{a}\nb:{b}')