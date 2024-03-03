import string
import random

def generate_password(length, include_numbers=True, include_lowercase=True, include_uppercase=True, begin_with_letter=True, include_symbols=True, no_similar_characters=True, no_duplicate_characters=True, no_sequential_characters=True):
    characters = ''
    if include_numbers:
        characters += string.digits
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_symbols:
        characters += '!";#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
    if no_similar_characters:
        characters = characters.translate(str.maketrans('', '', 'il1Lo0O'))
    if no_duplicate_characters:
        characters = ''.join(set(characters))
    if no_sequential_characters:
        characters = ''.join([characters[i] for i in range(len(characters)) if i == 0 or characters[i] != characters[i-1]])
    
    if begin_with_letter:
        first_char = random.choice(string.ascii_letters)
    else:
        first_char = random.choice(string.ascii_letters + string.digits + '!";#$%&\'()*+,-./:;<=>?@[]^_`{|}~')
    
    password = first_char + ''.join(random.choices(characters, k=length-1))
    return password

def get_user_preferences():
    length = int(input("Password Length: "))
    include_numbers = input("Include Numbers (y/n): ").lower() == 'y'
    include_lowercase = input("Include Lowercase Characters (y/n): ").lower() == 'y'
    include_uppercase = input("Include Uppercase Characters (y/n): ").lower() == 'y'
    begin_with_letter = input("Begin With A Letter (y/n): ").lower() == 'y'
    include_symbols = input("Include Symbols (y/n): ").lower() == 'y'
    no_similar_characters = input("No Similar Characters (y/n): ").lower() == 'y'
    no_duplicate_characters = input("No Duplicate Characters (y/n): ").lower() == 'y'
    no_sequential_characters = input("No Sequential Characters (y/n): ").lower() == 'y'
    return length, include_numbers, include_lowercase, include_uppercase, begin_with_letter, include_symbols, no_similar_characters, no_duplicate_characters, no_sequential_characters

def main():
    length, include_numbers, include_lowercase, include_uppercase, begin_with_letter, include_symbols, no_similar_characters, no_duplicate_characters, no_sequential_characters = get_user_preferences()
    password = generate_password(length, include_numbers, include_lowercase, include_uppercase, begin_with_letter, include_symbols, no_similar_characters, no_duplicate_characters, no_sequential_characters)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
    input('\n')