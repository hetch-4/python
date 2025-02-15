class warehouse:
    purpose = 'Storage'
    region = 'west'

w1 = warehouse()
print(w1.purpose, w1.region)

w2 = warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)