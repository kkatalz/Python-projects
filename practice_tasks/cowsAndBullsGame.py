import random

def generate_number():
    number = random.randint(1000, 9999)
    while len(set(str(number))) != 4:
        number = random.randint(1000, 9999)
    return number


def check_cows_and_bulls(number, guess):
    cows, bulls = 0, 0

    secret_number = str(number)
    guess = str(guess)

    for i, digit in enumerate(guess):

        if digit == secret_number[i]:
            bulls += 1

        elif digit in secret_number:
            cows += 1
    
    print(f"{cows} cows, {bulls} bulls")
    return bulls



def main():
    secret_number = int(generate_number())

    print("I've generated a 4-digit number with unique digits. Try to guess it.")   
    
    while True:
        guess = input("Guess: ").strip()

        try:
           if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
                raise ValueError
            
        except ValueError:
            print("Invalid input. Please enter a 4 digit unique number.")
            continue
        
        bulls = check_cows_and_bulls(secret_number, guess)
        if  bulls != 4:
            continue
        else:
            print(f"\nCongratulations! You've guessed the number {secret_number}.")
            break
        
if __name__ == "__main__":
    main()