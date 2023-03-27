from random import choice,  randint, sample

def Thief():
    
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    num1 = choice(numbers)
    num2 = choice(numbers)
    num3 = choice(numbers)
    num4 = choice(numbers)

    print("The pin code numbers are: " + num1, num2, num3, num4)
    print("=================================")


    pindigits = [num1, num2, num3, num4]

    pinsequence = sample(pindigits, len(pindigits))

    pincode = str(pinsequence)

    print("The actual pin is " + pincode)

Thief()
