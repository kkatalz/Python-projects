import random 
import os
import string 

made_guess_total = 0    
made_wrong_guess = 0 
tries_left = 6
correct_guess = 0
random_word = ""
guessed_part = []


def generate_random_word():

    global random_word, guessed_part

    dir_location = os.path.dirname(os.path.abspath(__file__))
    words_file = os.path.join(dir_location,"words.txt")

    with open(words_file, "r") as f:
        words_list = f.readlines()
        words_list = [word.strip() for word in words_list]
        random_word = random.choice(words_list)
        guessed_part = ["_"] * len(random_word)
        print("\n",random_word)
        print("---" * 5)

    return random_word

def show_guessed_part(random_word, guess):
    global guessed_part, tries_left, correct_guess
    guessed_part = list(guessed_part)

    if guess not in random_word: #banana
        tries_left -=1 
        print("Wrong guess")
    
    elif guess not in guessed_part: #b_n_n_
        correct_guess += 1
        print("Good guess")

        for i, letter in enumerate(random_word):
            if letter == guess: guessed_part[i] = guess
    
    elif guess in guessed_part:
        print("You already guessed that letter")
    
    guessed_part = ''.join(guessed_part)
    return print(guessed_part)


def make_guess(random_word):
    global made_guess_total, tries_left
    

    while True:
        if tries_left == 0:
            print(f"\nThe game is over. The secret word was: {random_word})")
            exit()
        
        elif "_" not in guessed_part:
           print(f"\nCongragularions! You guessed the word: {random_word}")
           exit()

        print(f"\nYou have {tries_left} tries left to guess the word!")
        guess = input("Enter a letter: ")
        if len(guess) > 1: 
            print("Enter only one letter.")
            continue
        elif guess not in string.ascii_lowercase:
            print("Enter only letters from a to z.")
            continue
        else:
            made_guess_total += 1
            show_guessed_part(random_word, guess)
       

    

def main():
    random_word = generate_random_word()
    make_guess(random_word)
        



if __name__ == "__main__":
    main()