for i in range(5):
    print(i)

x = int(input("enter a number:"))
print("These are the next ten numbers:")
l = []
l = range(x,x + 10)
for i in l:
    if i == l[0]:
        continue
    print(i)

a = ['Mary',"had", 'a',"little","lamb"]
for i in range(len(a)):
    print(i,a[i])