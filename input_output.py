year = 2016
event = 'Refurendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

s ='Hello World.'
print(str(s))
print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x)  + ', and y is ' + repr(y) + '...'
print(s)

hello = 'hello world\n'
hellos = repr(hello)
print(hello)
print(hellos)#repr adds quotes and backlashes

#the argument to repr() may be a python object
print(repr((x, y, ('spam','eggs'))))

