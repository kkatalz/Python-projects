import random 
import os
import string 

def choose_random_word():
    dir_location = os.path.dirname(os.path.abspath(__file__))
    words_file = os.path.join(dir_location,"words.txt")
    with open(words_file, "r") as f:
        words_list = f.readlines()
        words_list = [word.strip() for word in words_list]
        chosen_word = random.choice(words_list)
        print(chosen_word)
        print("---" * 5)

    return chosen_word

def show_guessed_part(random_word, guess):
    
    gueesed_part = ""
    for letter in random_word:
        if letter != guess: gueesed_part += "_"
        else: gueesed_part += guess
    return gueesed_part

def make_guess(chosen_word):

    correct_guess = 0
    while True:
        guess = input("Enter a letter: ")
        if len(guess) > 1: 
            print("Enter only one letter.")
            continue
        elif guess not in string.ascii_lowercase:
            print("Enter only letters from a to z.")
            continue
        elif guess in chosen_word:
            print("Good guess")
            correct_guess += 1
            print(show_guessed_part(chosen_word, guess))

def main():
    chosen_word = choose_random_word()
    make_guess(chosen_word)
        



if __name__ == "__main__":
    main()