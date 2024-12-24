# if two images match you win two times more
# if 3 match then you win 10 times more

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