import random 
import re
import string

def generate_password(password_length, uppercase_letters, numbers, special_characters):
    lowercase_letters_list = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers_list = '0123456789'
    special_characters_list = '!@#$%^&*()-+'
    all_characters = lowercase_letters_list
    password =[]

    if uppercase_letters == 'y':
        all_characters += uppercase_letters_list
        password.append(random.choice(uppercase_letters_list))
    if numbers == 'y':
        all_characters += numbers_list
        password.append(random.choice(numbers_list))
    if special_characters == 'y':
        all_characters += special_characters_list
        password.append(random.choice(special_characters_list))

    remaining_length = password_length - len(password)
    password += [random.choice(str(all_characters)) for _ in range(remaining_length)]
    random.shuffle(password)
    password = ''.join(password)
    print(f"Generated password is {str(password)}")

def main():

    while True:
        try:
            password_length = int(input("Enter password length (at least 5 characters long): ").strip())
            if password_length < 4: 
                raise ValueError
            break
        except ValueError:
            print("Invalid length")
            continue
 
   
    while True:
        uppercase_letters = input("Include uppercase letters? (y/n): ").strip().lower()
        if not (uppercase_letters == 'y' or uppercase_letters == 'n'):
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        else: break

    while True:        
        numbers = input("Include numbers? (y/n): ").strip().lower()
        if not (numbers == 'y' or numbers == 'n'):
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        else: break
    
    while True:
        special_characters = input("Include special characters? (y/n): ").strip().lower()
        if not (special_characters == 'y' or special_characters == 'n'):
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        else: break

    generate_password(password_length, uppercase_letters, numbers, special_characters)

if __name__ == '__main__':
    main()  