import random

def number_game(x, y, attempts_list): 

    random_number = random.randint(x, y)
    attempts_count_total = 10
    attempts_count_made = 0
    print("Secretly: your number is: ", random_number)
    print(f"You have {attempts_count_total} attempts to guess the number!")
    while attempts_count_made != attempts_count_total:
        try:
            user_input = int(input("Guess the number between 1 and 100: "))

            if user_input < random_number:
                print("Too low!")
            elif user_input > random_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number!")
                break

            attempts_count_made += 1
        except ValueError:
            print("Please enter a valid number")

    if attempts_count_made == attempts_count_total:
        print("You have used all your attempts!")
        print(f"The number was: {random_number}")
    
    attempts_list.append(attempts_count_made)




def game_mode(attempts_list):
    user_start = int(input("Do you want to specify the range of numbers? (1 - yes, 0 - no): "))
    if user_start == 1:
        specify_x = int(input("Enter the lower bound of the range: "))
        specify_y = int(input("Enter the upper bound of the range: "))
        number_game(specify_x, specify_y, attempts_list)
    else:
        number_game(1, 100, attempts_list)
    
    play_again(attempts_list)

def play_again(attempts_list):
    user_input = int(input("Do you want to play again? (1 - yes, 0 - no): "))
    if user_input == 1:
        game_mode(attempts_list)
    else:
        print("Thanks for playing!")
        if attempts_list:
            print(f"Minimum attempts made: {min(attempts_list)}")
            print(f"Maximum attempts made: {max(attempts_list)}")


attempts_list = []
game_mode(attempts_list)