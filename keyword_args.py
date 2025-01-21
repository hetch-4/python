def parrot(volts, state = 'a stiff', action = 'voom', type = 'Norwiegian Blue'):
    print("-- this parrot wouldn't", action, end =' ')
    print("if you put", volts, "volts through it.")
    print("--Lovely plumage, the",type)
    print("--It's ",state,"!")

parrot(10000)
parrot(action = "Boom", volts = 10000)