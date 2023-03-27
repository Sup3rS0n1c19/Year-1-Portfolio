import random
import string

def Generator():

    CharacterList = ''
    CharacterList += string.ascii_lowercase
    CharacterList += string.ascii_uppercase
    CharacterList += string.digits
    CharacterList += string.punctuation


    passlength = int(input("Please enter the numerical value of characters you desire in your password: "))
    if passlength < 8:
        print("Please enter your password length again")
        passlength = int(input("Please enter the numerical value of characters you desire in your password again: "))


    password = []



    for i in range(passlength):
        RandomChar = random.choice(CharacterList)
        password.append(RandomChar)


    print("The random password is " + "".join(password))



Generator()
    



    
