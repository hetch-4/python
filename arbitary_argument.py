def concat(*args, sep="/"):
    print( sep.join(args))
 
concat("earth","mars",'venus')
concat('earth','mars','venus',sep = '.')

#unpacking argument list 
args = [3,6]
x = list(range(*args))
print(x)

def parrot(voltage, state = 'a stiff', action = 'Voom'):
    print("--this parrot wouldn't", action, end = ' ')
    print("if you put ", voltage, "volts through it.", end = " ")
    print("E's",state, "!")

d = {"voltage":"four million", "state" :"bleedin' demised", "action":"Voom"}
parrot(**d)

#lambda expressions
#are just like nested functioin in a function
def make_incrementor(n):
    return lambda x:x + n

f = make_incrementor(42)
print(f(1))

#lambda can be used to pass a small function in statement
pairs = [(1,'one'),(2,'two'),(3,'three'),(4,"four")]
pairs.sort(key = lambda pair:pair[1])
print(pairs)
