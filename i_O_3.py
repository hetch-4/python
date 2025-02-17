for x in range(1, 11):
    print('{0:4d} {1:4d} {2:4d}'.format(x, x*x, x*x*x))





table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{'+ k +'};' for k in table.keys()])
print(message.format(**table))