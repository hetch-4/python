text = 'Hello World!'
shift = 3
alphabet = 'abcdefghijklmnopqrstvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index + shift]
print(shifted)
