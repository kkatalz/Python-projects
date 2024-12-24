# if two images match you win two times more
# if 3 match then you win 10 times more
import random
current_balance = 0
bet_amount = 0

choice_icons = ("🍉", "🍋", "🍇", "🥑", "🍗")

def choose_icons():
    icons_list = [random.choice(choice_icons) for _ in range(3)]
    print(f"{icons_list[0]} | {icons_list[1]} | {icons_list[2]}")
    return icons_list


def calculate_current_balance(winning_money):
    global current_balance
    current_balance += (winning_money - bet_amount)   
    current_balance = round(current_balance,3)

def check_victory(icons_list):
    winning_money = 0    
    first_icon, sec_icon, trd_icon = icons_list

    if first_icon == sec_icon == trd_icon:
        winning_money = bet_amount * 10
        print(f"You won {winning_money}!")
        calculate_current_balance(winning_money)


    elif first_icon == sec_icon or sec_icon == trd_icon or first_icon == trd_icon:
        winning_money = bet_amount * 2
        print(f"You won {winning_money}!")
        calculate_current_balance(winning_money)
    
    else:
        calculate_current_balance(winning_money)
        print("You lost!")
        if current_balance <=0:
            print("You are out of money! Game is over.")
            exit()
    
    return current_balance

def get_bet_amount():
    global bet_amount
    while True:
            try:
                bet_amount = float(input("Enter your bet amount: $").strip())
                if bet_amount > current_balance or bet_amount < 1:    
                    print(f"Invalid bet amount. You can bet between $1 and ${current_balance}")   
                else:
                    return

            except ValueError:
                print("Please enter a valid number for the bet amount")

def play_again():
    while True:
            play_again_answer = input("\nDo you want to play again? (y/n): ").strip().lower()

            if play_again_answer in ('y', 'yes'):
                return
            elif play_again_answer in ('n', 'no'):
                print(f"\nYour current balance is {current_balance}. \nGame is over.")
                exit()
            else:
                print("Incorrect input")
                continue

def game():
    while True:
        print(f"\nCurrent ballance: ${current_balance}")
        get_bet_amount()
        icons_list = choose_icons()
        check_victory(icons_list)
        play_again()

def get_staring_balance():
    global current_balance
    while True:
        try:
            balance = float(input("Enter your starting balance: $").strip())
            if balance <= 0:
                print("Balance must be a positive number") 
            else:
                current_balance = balance
                return
        except ValueError:
            print("Please enter a valid number")

def main():
    get_staring_balance()
    game()



if __name__ == "__main__": 
    main()