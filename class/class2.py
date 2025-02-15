class dog:
    kind = 'canine'  #variable shared by all instances

    def __init__(self, name):
        self.name = name #variable unique to each instance
        self.tricks = []  # new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = dog('fido')
e = dog('buddy')
print(d.kind, d.name)   
print(e.kind, e.name)
#above both share kind 'canine'
#but have unique names that were assigned

d.add_trick('roll over')
d.add_trick('handshake')
e.add_trick('play dead')

print(d.tricks)
print(e.tricks)

