user_input = input("Please select a word ").lower()

if user_input == user_input[::-1]:
    print("This word is a palindrome")
else:
    print("This word isn't a palindrome")
