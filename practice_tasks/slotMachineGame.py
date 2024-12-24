# if two images match you win two times more
# if 3 match then you win 10 times more
import random
current_balance = 0

choice_icons = ("🍉", "🍋", "🍇", "🥑", "🍗")

def choose_icon():
    first_icon = random.choice(choice_icons)
    sec_icon = random.choice(choice_icons)
    trd_icon = random.choice(choice_icons)
    print(f"\n{first_icon} | {sec_icon} | {trd_icon}")

    icons_set = (first_icon, sec_icon, trd_icon)
    return icons_set

def check_victory(set_icons, starting_balance, bet_amount):
    global current_balance
    winning_money = 0

    starting_balance = int (starting_balance)
    bet_amount = int(bet_amount)
    
    first_icon, sec_icon, trd_icon = set_icons

    if first_icon == sec_icon == trd_icon:
        winning_money = bet_amount * 10
        print(f"You won {winning_money}!")

    elif first_icon == sec_icon or sec_icon == trd_icon or first_icon == trd_icon:
        winning_money = bet_amount * 2
        print(f"You won {bet_amount * 2}!")
    
    else:
        print("You lost!")
    
    current_balance = int(current_balance) - bet_amount + winning_money
    return current_balance

def game(starting_balance):
    play_again = True

    while play_again:
        starting_balance = int(starting_balance) 
        print(f"\nCurrent ballance: ${current_balance}")

        while True:
            bet_amount = input("Enter your bet amount: $").strip()
            if not bet_amount.isdigit():
                print("Please enter a valid number for the bet amount")
                continue

            elif int(bet_amount) > starting_balance or int(bet_amount) < 1:    
                print(f"Invalid bet amount. You can bet between $1 and ${current_balance}")
                continue
            break


        set_icons = choose_icon()
        check_victory(set_icons, starting_balance, bet_amount)

        while True:
            play_again_answer = input("Do you want to play again? (y/n): ").strip().lower()

            if play_again_answer in ('y', 'yes'):
                break
            elif play_again_answer in ('n', 'no'):
                print(f"\nYour current balance is {current_balance}. \nGame is over.")
                exit()
            else:
                print("Incorrect input")
                continue


def main():
    global current_balance
    while True:
        starting_balance= input("Enter your starting balance: $").strip()
        if not starting_balance.isdigit():
            print("Please enter a valid number")
            continue
        elif int(starting_balance) <= 0:
            print("Balance must be a positive number") 
            continue

        current_balance = starting_balance
        break
    game(starting_balance)



if __name__ == "__main__": 
    main()