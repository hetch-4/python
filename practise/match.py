import random
def https_error(status):
    match status:
        case 400:
            print("bad request")
        case 404:
            print('Not found')
        case 418:
            print( "I'm a teapot")
        #combine several literals in a single pattern using | 
        case 401 | 403 | 404:
            print("Not allowed")

        case _:
            print("somethin's wrong with the internet")

stat = random.choice([400,404,418,401,403])
print(stat)
https_error(stat)

