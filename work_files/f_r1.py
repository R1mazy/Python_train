from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters

def generate_password(user_input, length):
    characters = list(user_input)

    has_lowercase = any(char.islower() for char in characters)
    has_uppercase = any(char.isupper() for char in characters)
    has_digit = any(char.isdigit() for char in characters)

    if has_lowercase == False:
        characters += [choice(ascii_lowercase)]
    if has_uppercase == False:
        characters += [choice(ascii_uppercase)]
    if has_digit == False:
        characters += [choice(digits)]

    while length > len(characters):
        characters.append(choice(user_input + digits + ascii_letters))
        shuffle(characters)

    return ''.join(characters)

user_input, length = input().split()
length = int(length)

print(generate_password(user_input, length))