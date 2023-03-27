def Menu():
    print("||=============================||")
    print("||                             || ")
    print("||                             || ")
    print("||  1) Create an event         || ")
    print("||  2) Edit an event           || ")
    print("||  3) View calendar           || ")
    print("||                             || ")
    print("||                             || ")
    print("||=============================||")

    UserChoice = int(input("Please enter a number between 1 and 3 "))
    if UserChoice == 1:
        CreateEvent()
    elif UserChoice == 2:
        EditEvent()
    elif UserChoice == 3:
        Calendar()
    else:
        print("Please enter a integer between 1 and 3 ")

def CreateEvent():
    Event = input("Would you like to create an event? ")
    if Event == "Yes":
        EventDate = input("When is this event due to take place? ")
    elif Event == "No":
        menu()
    else:
        input("Please respond with 'Yes' or 'No' ")

#def EditEvent():
    
Menu()
