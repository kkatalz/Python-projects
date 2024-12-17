import random

# RULES:
# 1. The game is played between two players. One player is the coputer and the other is the user.
# 2. The computer generates a 4-digit number with unique digits.
# 3. The user has to guess the number.
# 4. If the user's guess has a digit in the correct position, it's a "bull".
# 5. If the user's guess has a digit in the wrong position, it's a "cow".
# 6. The user continues to guess until they guess the number correctly.

def generate_number():
    number = random.randint(1000, 9999)
    while len(set(str(number))) != 4:
        number = random.randint(1000, 9999)
    return number


def check_cows_and_bulls(number, guess):
    cows, bulls = 0, 0

    secret_number = str(number)
    guess = str(guess)

    bulls = sum([1 for i in range(4) if guess[i] == secret_number[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret_number]) - bulls

    print(f"{cows} cows, {bulls} bulls")
    return bulls



def main():
    secret_number = int(generate_number())

    print("I've generated a 4-digit number with unique digits. Try to guess it.")   
    
    while True:
        guess = input("Guess: ").strip()

        
        if guess.isdigit() and len(guess) == 4 and len(set(guess)) == 4:
            bulls = check_cows_and_bulls(secret_number, guess)
            if  bulls == 4:
                print(f"\nCongratulations! You've guessed the number {secret_number}.")
                break

        else:
            print("Invalid input. Please enter a 4 digit unique number.")
        
if __name__ == "__main__":
    main()