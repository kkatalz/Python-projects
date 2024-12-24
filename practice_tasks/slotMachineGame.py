# if two images match you win two times more
# if 3 match then you win 10 times more
import random

choice_icons = ("🍉", "🍋", "🍇", "🥑", "🍗")

def choose_icon():
    first_icon = random.choice(choice_icons)
    sec_icon = random.choice(choice_icons)
    trd_icon = random.choice(choice_icons)
    print(f"{first_icon} | {sec_icon} | {trd_icon}")

    icons_set = (first_icon, sec_icon, trd_icon)
    return icons_set



def game(starting_balance):
    starting_balance = int(starting_balance) 
    print(f"\nCurrent ballance: ${starting_balance}")
    
    while True:
        bet_amount = input("Enter your bet amount: $").strip()
        if not bet_amount.isdigit():
            print("Please enter a valid number for the bet amount")
            continue

        elif int(bet_amount) > starting_balance or int(bet_amount) < 1:    
            print(f"Invalid bet amount. You can bet between $1 and ${starting_balance}")
            continue
        break

    set_icons = choose_icon()
    # check_victory(set_icons, starting_balance, bet_amount)




def main():
    while True:
        starting_balance= input("Enter your starting balance: $").strip()
        if not starting_balance.isdigit():
            print("Please enter a valid number")
            continue
        elif int(starting_balance) <= 0:
            print("Balance must be a positive number") 
            continue
        break
    game(starting_balance)



if __name__ == "__main__": 
    main()