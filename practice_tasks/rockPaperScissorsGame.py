import random
    
choice_icons = {
    "r": "🪨",  # Stone
    "p": "📄",  # Paper
    "s": "✂️"  # Scissors
}

choices = ("r", "p", "s")

def rock_paper_scissors_game():
    user_choice = user_choice_input(input("Rock, paper or scissors? (r/p/s): ").lower())
    computer_choice = random.choice(choices)


    print(f"You chose {choice_icons[user_choice]}")
    print(f"Computer chose {choice_icons[computer_choice]}")
    print(rock_paper_scissors_winner(user_choice, computer_choice))

    play_again()

def user_choice_input(user_choice):

    while user_choice not in choices:
            print("Invalid choice")
            user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
    
    return user_choice

def rock_paper_scissors_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == "r" and computer_choice == "s") or 
         (user_choice == "s" and computer_choice == "p") or 
         (user_choice == "p" and computer_choice == "r")) :
        return "You win!"
    
    elif ((user_choice == "r" and computer_choice == "p") or
         (user_choice == "s" and computer_choice == "r" ) or 
         (user_choice == "p" and computer_choice == "s")):
        return "You lose!"
    


def play_again():
    user_input = input("Do you want to play again? (y/n): ").lower()
    if user_input == "y":
        rock_paper_scissors_game()
    else:
        print("Thanks for playing!")



# start the game 
rock_paper_scissors_game()