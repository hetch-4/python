class bag:
    def __init__(self):
        self.data=[]

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

x = bag()
x.add('Gucci')
x.addtwice('kasuku')
print(x.data)
