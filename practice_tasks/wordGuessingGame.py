import random 
import os

def main():
    dir_location = os.path.dirname(os.path.abspath(__file__))
    words_file = os.path.join(dir_location,"words.txt")
    with open(words_file, "r") as f:
        words_list = f.readlines()
        words_list = [word.strip() for word in words_list]
        chosen_word = random.choice(words_list)
        print(chosen_word)
        print("---" * 5)
        



if __name__ == "__main__":
    main()