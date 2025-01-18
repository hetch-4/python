#control flow 

#if statement
x = int(input("Please enter an integer:"))

if x < 0:
    x = 0
    print ('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')

#for statement
words = ['car','window','defenestrate']

for x in words:
    print( x , len(x) )

    #modify  a collection while while iterating through it to create a new sample
users = {'Hans':'active','Eleonore':"inactive",'XiaXo':'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(users)
print(active_users)
