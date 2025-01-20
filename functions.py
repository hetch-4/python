#defining of functions
    #the Fibonaci series
print("Fibonaci series upto n:\n")
def fib(n): #def introduses a function  fib is the function name 
    #series less than n
    a ,b = 0, 1  #
    while  a<n:
        print(a, end = ' ')
        a,b = b, a+b
        print()
 
x = int(input("Enter the numbers n:")) #user input of the limit n of the series
fib(x) #calling the function 