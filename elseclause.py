#finding a prime number
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,"equals",x,'*',n//x)
            break
    else:
        print(n,"is a prime number")


#pass statements
class emptyclass:
    pass

def initlog(*args):
    pass # remember to implement this !

