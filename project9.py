number = input("Enter a number: ")

digit_count = sum(character.isdigit() for character in number)

print(f"The number has {digit_count} digits.")