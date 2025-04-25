import random
import string
alphabet = string.ascii_letters + string.digits + string.punctuation
quant = 0
many = 0
b = ''
while quant <= 0 or many <= 0:
    quant = int(input("Enter the length of the password: "))
    many = int(input("Enter the number of passwords to generate: "))

    a = input("Do you want add some especifc word or letter? (y/n): ")
    if a == 'y':
        b = input("Enter the word or letter: ")
    elif a == 'n':
        pass
    else:
        print("Invalid option.")

def password_generator(length, quantity, wordused):
    passwords = []
    password = ''
    for i in range(quantity):
        password = ''
        if wordused != '':
            password = password + wordused
        elif wordused == '':
            pass
        for j in range(length-len(wordused)):
            password = password + random.choice(alphabet)
        passwords.append(password)

    return passwords

if b != '':
    lista = password_generator(quant, many, b)
else:
    lista = password_generator(quant, many, '')

for i in range(len(lista)):
    print(lista[i])
print("Password(s) generated successfully.")
