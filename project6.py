character = input("Enter one character: ")

if len(character) == 1 and character.isalpha():
    print("It is an alphabet letter.")
else:
    print("It is not an alphabet letter.")