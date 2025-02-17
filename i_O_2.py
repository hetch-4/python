print('we are th {} who say {}'.format('knights', 'Ni!'))

print('{0} and {1}'.format('spam', 'eggs'))     #prints spam first
print('{1} and {0}'.format('spam', 'eggs'))      #prints eggs first
    #positional arguments

print('This {food} is {adjective}.'
      .format( food = 'spam', adjective = 'absolutely horrible'))
    #keyword arguments

print('the story of {0}, {1}, and {other}.'
      .format('Bill', 'Manfred', other='Georg'))
    #combine positional and keyword arguments

table = {'joker':4127, 'batman':4098, 'Dcab':8637678}
print('Joker: {joker:d}, batman:{batman:d}, Dcab: {Dcab:d}'.format(**table))
