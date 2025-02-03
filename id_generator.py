import secrets
def get_id():
    idno = input("Enter ID: ")
    characters = list(idno.upper())

    a = len(characters)
    if a != 4:
        print("Error : Invalid ID")

    print("Valid")

#get_id()

def verify_id(idno):
    char = list(idno)
    a = char[0]
    if a != 'S':
        print("Errpr: Invalid id") 

    b = char[1]
    if b not in ['A','B','C','D']:
        print("Error :not a valid ID")
    
    c = char[2]
    if c != '#':
        print('Error :Ivalid id')

    d = char[3]
    if d not in range(4):
        print("Error : Invalid Id")

verify_id('BA#4')

